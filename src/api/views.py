from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.reponse import Response

from rabble.models import *
from .serializers import *

@api_view(['GET'])
def subrabble_list(request):
    if request.method == 'GET':
        subrabbles = Subrabble.objects.all()
        serializer = SubrabbleSerializer(subrabbles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubrabbleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def subrabble_detail(request, pk):
    try:
        subrabble = Subrabble.objects.get(pk=pk)
    except Subrabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SubrabbleSerializer(subrabble)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SubrabbleSerializer(subrabble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SubrabbleSerializer(subrabble, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subrabble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    