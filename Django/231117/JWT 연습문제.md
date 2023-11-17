# Access Token이 유효한 경우에만 접근이 가능한 마이페이지를 만들어주세요.

1. 로그인하여 Access Token을 발급받습니다.
2. 마이페이지 접속시 header에 Access Token을 담아보냅니다. Access Token이 유효한 경우에만 마이페이지에 접근이 가능합니다.
3. 마이페이지에 접속하면(포스트맨 또는 다른 API 툴로 하셔도 됩니다.) "반갑습니다, {유저이메일}님!"이 화면에 출력되도록 해주세요.

# 구현되어야할 엔드 포인트는(API) 아래와 같습니다.

/account/join # 회원가입
/account/login # 로그인
/account/logout # 로그아웃
/account/mypage # 로그인한 사용자만 확인가능


python -m venv venv # 가상환경 생성

source venv/Scripts/activate # mac, linux
# .\venv\Scripts\activate # window

pip install django # django 설치

django-admin startproject project . # project 프로젝트 생성

python manage.py startapp accounts # accounts 앱 생성

# settings.py > INSTALLED_APPS에 새로 생성한 앱 추가

# accounts/managers.py
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

GENDER_CHOICES = (
    ('male', '남자'),
    ('female', '여자'),
)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email

# settings.py 에 추가
AUTH_USER_MODEL = 'accounts.CustomUser'

# 마이그레이션

python manage.py makemigrations
python manage.py migrate

# accounts/admin.py
from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)




# 필요한 라이브러리

djangorestframework # RESTful API 개발
dj-rest-auth # 인증 및 사용자 관리 구현(로그인, 로그아웃, 회원가입 및 소셜 로그인)
django-allauth # 다양한 인증 및 회원가입 옵션을 제공 (사용자 인증, 회원가입, 비밀번호 재설정 및 소셜 로그인)
djangorestframework-simplejwt # JSON Web Token (JWT) 인증을 구현



# settings.py에 추가

INSTALLED_APPS = [
...
    # 설치한 라이브러리들
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
...
]

from datetime import timedelta

... 생략 ...

# dj-rest-auth
REST_USE_JWT = True # JWT 사용 여부
JWT_AUTH_COOKIE = 'my-app-auth' # 호출할 Cookie Key 값
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' # Refresh Token Cookie Key 값

# django-allauth
SITE_ID = 1 # 해당 도메인 id
ACCOUNT_UNIQUE_EMAIL = True # User email unique 사용 여부
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # 사용자 이름 필드 지정
ACCOUNT_USERNAME_REQUIRED = False # User username 필수 여부
ACCOUNT_EMAIL_REQUIRED = True # User email 필수 여부
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 로그인 인증 수단
ACCOUNT_EMAIL_VERIFICATION = 'none' # email 인증 필수 여부

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # AccessToken 유효 기간 설정
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),  # RefreshToken 유효 기간 설정
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}



# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls"))
]

# accounts/urls.py
from django.urls import path, include
from .views import mypage_view

urlpatterns = [
    path('mypage/', mypage_view), #요구사항에 있던 로그인시에 보여줄 페이지
    path('join/', include('dj_rest_auth.registration.urls')), #회원가입
    path('', include('dj_rest_auth.urls')), #login과 logout은 dj_rest_auth로 처리됨
]


# accounts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 인증되었을시
def mypage_view(request):
    # request.user는 인증된 사용자의 정보를 담고 있습니다.
    # request에 POST에 담긴 data를 출력합니다.
    print(request.data)
    content = {'message': '반갑습니다', 'user': str(request.user)}
    return Response(content)

