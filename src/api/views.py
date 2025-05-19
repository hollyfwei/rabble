from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rabble.models import *
from .serializers import *

@api_view(['GET'])
def subrabble_list(request):
    # Gets all the subRabbles
    if request.method == 'GET':
        subrabbles = Subrabble.objects.all()
        serializer = SubrabbleSerializer(subrabbles, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def subrabble_detail(request, identifier):
    try:
        subrabble = Subrabble.objects.get(identifier=identifier)
    except Subrabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Gets the subRabble with the given identifier
    if request.method == 'GET':
        serializer = SubrabbleSerializer(subrabble)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_list(request, identifier):
    try:
        subrabble = Subrabble.objects.get(identifier=identifier)
    except Subrabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Gets all the posts in the given subRabble
    if request.method == 'GET':
        posts = Post.objects.filter(subrabble=subrabble)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # Creates a new post in the given subRabble
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def post_detail(request, identifier, pk):
    try:
        subrabble = Subrabble.objects.get(identifier=identifier)
    except Subrabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    try:
        post = Post.objects.get(pk=pk, subrabble=subrabble)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Gets the post with primary key pk
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Updates attributes of the post with primary key pk
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Deletes the post with priamry key pk
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubrabbleList(generics.ListCreateAPIView):
    queryset = Subrabble.objects.all()
    serializer_class = SubrabbleSerializer

class SubrabbleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subrabble.objects.all()
    serializer_class = SubrabbleSerializer
    lookup_field = 'identifier'

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        return Post.objects.filter(subrabble__identifier=identifier)
    
    def perform_create(self, serializer):
        identifier = self.kwargs['identifier']
        subrabble = Subrabble.objects.get(identifier=identifier)
        serializer.save(subrabble=subrabble)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        identifier = self.kwargs['identifier']
        return Post.objects.filter(subrabble__identifier=identifier)
    