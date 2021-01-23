from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAdmin, IsTeacher


class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsTeacher)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
