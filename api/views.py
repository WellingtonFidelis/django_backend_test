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
    try:
        queryset = FormTest.objects.all()
        serializer = FormTestSerializer(queryset, many=True)
        response = {
                'status': 'Ok',
                'message': 'List of register called.',
                'result': serializer.data
                }
        return Response(response, status=status.HTTP_200_OK)
    
    except:
        response = {
                'status': 'Fail',
                'message': 'Ops, I can not help you',
                'result': serializer.errors
                }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def formListDetail(request, pk):
    try:
        queryset = FormTest.objects.get(id=pk)
        serializer = FormTestSerializer(queryset, many=False)
        response = {
                'status': 'Ok',
                'message': 'Register called.',
                'result': serializer.data
                }
        return Response(response, status=status.HTTP_200_OK)

    except:
        response = {
                'status': 'Fail',
                'message': 'Ops, I can not help you',
                'result': serializer.errors
                }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def formCreate(request):
    serializer = FormTestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        response = {
                'status': 'Ok',
                'message': 'Register created.',
                'result': serializer.data
                }
        return Response(response, status=status.HTTP_201_CREATED)

    response = {
            'status': 'Fail',
            'message': 'Ops, I can not help you',
            'result': serializer.errors
            }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def formUpdate(request, pk):
    queryset = FormTest.objects.get(id=pk)
    serializer = FormTestSerializer(queryset, data=request.data)

    if serializer.is_valid():
        serializer.save()
        response = {
                'status': 'Ok',
                'message': 'Register updated.',
                'result': serializer.data
                }
        return Response(response, status=status.HTTP_202_ACCEPTED)

    response = {
            'status': 'Fail',
            'message': 'Ops, I can not help you',
            'result': serializer.errors
            }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def formDelete(request, pk):
    try:
        queryset = FormTest.objects.get(id=pk)
        queryset.delete()
        response = {
                'status': 'Ok',
                'message': 'Register deleted.',
                'result': f'{queryset.first_name} {queryset.last_name}'
                }
        return Response(response, status=status.HTTP_200_OK)

    except:
        response = {
            'status': 'Fail',
            'message': 'Ops, I can not help you',
            'result': 'Not Found'
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

