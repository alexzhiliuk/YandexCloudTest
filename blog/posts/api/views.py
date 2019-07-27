from rest_framework import generics
from posts.models import Post, Category
from posts.api.serializers import PostSerializer, CategorySerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(generics.ListAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryView(generics.ListAPIView):
	serializer_class = PostSerializer

	def get_queryset(self):
		category = self.kwargs['category']
		return Post.objects.filter(category__title=category)