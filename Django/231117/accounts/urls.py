from django.urls import path, include
from .views import mypage_view

urlpatterns = [
    path('mypage/', mypage_view),
    path('join/', include('dj_rest_auth.registration.urls')),
    path('', include('dj_rest_auth.urls')),
]