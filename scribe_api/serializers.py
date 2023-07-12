# To convert the Model object to an API-appropriate format like JSON with ModelSerializer class

from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'desc', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'desc', 'published', 'created_at', 'updated_at', 'user', 'category']


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'desc', 'published', 'user', 'category']


class UpdatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'desc', 'published', 'category']