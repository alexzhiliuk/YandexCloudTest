from django.contrib.auth.models import User
from posts.models import Post, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ["slug", "title"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'category', 'author', 'created']