from rest_framework import status, permissions, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, CreatePostSerializer, UpdatePostSerializer

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [] 
    search_fields = ['name', 'desc']
    ordering_fields = ['', 'created_at', 'updated_at'] 

class PostViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['published', 'user']  
    search_fields = ['title', 'desc']
    ordering_fields = ['title', 'created_at', 'updated_at']  # Fields to order by
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializer
        elif self.action == 'create':
            return CreatePostSerializer
        elif self.action == 'update':
            return UpdatePostSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ['list', 'retrieve']:
            queryset = queryset.select_related('category')
        return queryset

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset().filter(user=request.user.id))
    #     page = self.paginate_queryset(queryset)

    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def create(self, request, *args, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['put'], permission_classes=[permissions.IsAuthenticated])
    # def set_published(self, request, pk=None):
    #     post = self.get_object()
    #     post.published = not post.published
    #     post.save()
    #     serializer = self.get_serializer(post)
    #     return Response(serializer.data, status = status.HTTP_200_OK)