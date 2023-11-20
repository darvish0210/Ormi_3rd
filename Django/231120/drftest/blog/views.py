from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import IsUserOrRestricted



class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsUserOrRestricted]

    def perform_create(self, serializer):
        # 현재 로그인 한 user가 post의 author에 자동으로 입력되도록 재정의
        # serializer(PostSerializer)에 author라는 이름을 통해 self.request.user가 전달된다.
        serializer.save(author=self.request.user)