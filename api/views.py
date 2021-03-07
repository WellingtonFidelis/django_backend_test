from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from .models import FormTest
from .serializers import FormTestSerializer


# Create your views here.
# []create a status for all responses
#

@api_view(['GET'])
def formList(resquest):
    queryset = FormTest.objects.all()
    serializer = FormTestSerializer(queryset, many=True)
    response = serializer.data
    return Response(response)

@api_view(['GET'])
def formListDetail(request, pk):
    queryset = FormTest.objects.get(id=pk)
    serializer = FormTestSerializer(queryset, many=False)
    response = serializer.data
    return Response(response)

@api_view(['POST'])
def formCreate(request):
    serializer = FormTestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def formUpdate(request, pk):
    queryset = FormTest.objects.get(id=pk)
    serializer = FormTestSerializer(queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def formDelete(request, pk):
    queryset = FormTest.objects.get(id=pk)
    queryset.delete()

    return Response('Deleted')
