from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import models
from . import serializers


class CustomTokenObtainPairView(TokenObtainPairView):
    @extend_schema(
        tags=["user management"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @extend_schema(
        tags=["user management"]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RegisterView(APIView):
    @extend_schema(
        request=serializers.UserSerializer,
        responses={201: serializers.UserSerializer, 400: None},
        tags=["user management"]
    )
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogList(APIView):
    def get(self, request):
        blogs = models.Blog.objects.all()
        serializer = serializers.BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(APIView):
    def get_object(self, pk):
        try:
            return models.Blog.objects.get(pk=pk)
        except models.Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        blog = self.get_object(pk)
        if blog is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, pk):
        blog = self.get_object(pk)
        if blog is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        blog = self.get_object(pk)
        if blog is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        if blog is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)