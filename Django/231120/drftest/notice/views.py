from rest_framework.viewsets import ModelViewSet

from .models import Notice
from .serializers import NoticeSerializer
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsLoginOrRestricted


class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    permission_classes = [IsLoginOrRestricted]
    # GET 요청 - 모든 사용자 접근 가능하도록 설정
    # 로그인 한 인증 유저만 POST 가능
    # 로그인 한 인증 유저가 본인이 작성한 글에만 DELETE, PUT 가능

    def perform_create(self, serializer):
        # 현재 로그인 한 user가 post의 author에 자동으로 입력되도록 재정의
        # serializer(PostSerializer)에 author라는 이름을 통해 self.request.user가 전달된다.
        serializer.save(author=self.request.user)