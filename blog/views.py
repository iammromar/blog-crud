from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializers

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
