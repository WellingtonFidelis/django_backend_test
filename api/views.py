from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from .models import FormTest
from .serializers import FormTestSerializer


# Create your views here.
# -[x]create a status for all responses
# -[x]rewriting api using class-based views
#

class FormTestViewSet(viewsets.ModelViewSet):
   
    def list(self, request, *args, **kwargs):
        queryset = FormTest.objects.all()
        serializer_class = FormTestSerializer(queryset, many=True)

        response = {
                'status': 'Ok',
                'message': 'Registers called.',
                'result': serializer_class.data
                }
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer_class = FormTestSerializer(data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()
            response = {
                'status': 'Ok',
                'message': 'Register created.',
                'result': serializer_class.data
                }
            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status': 'Fail',
            'message': 'Ops, I can not help you',
            'result': serializer_class.errors
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, **kwargs):
        try:
            queryset = FormTest.objects.get(id=pk)
            serializer_class = FormTestSerializer(queryset, many=False)
            response = {
                    'status': 'Ok',
                    'message': 'Register called',
                    'result': serializer_class.data
                    }
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {
                'status': 'Fail',
                'message': 'Ops, I can not help you',
                'result': f'I can not found any register with id= {pk}'
                }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk, **kwargs):
        queryset = FormTest.objects.get(id=pk)
        serializer_class = FormTestSerializer(queryset, data=request.data)

        if serializer_class.is_valid():
            serializer_class.save()
            response = {
                'status': 'Ok',
                'message': 'Register updated.',
                'result': serializer_class.data
                }
            return Response(response, status=status.HTTP_202_ACCEPTED)

        response = {
            'status': 'Fail',
            'message': 'Ops, I can not help you',
            'result': serializer_class.errors
            }
        return Response(response, status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self, request, pk, **kwargs):
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
