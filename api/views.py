from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FormTest
from .serializers import FormTestSerializer


# Create your views here.

class FormTestViewSet(viewsets.ModelViewSet):
    queryset = FormTest.objects.all()
    serializer_class = FormTestSerializer

    @action(detail=True, methods=['GET'])
    def createRegister(self, request, *args, **kwargs):
        form = self.get_object()
        return Response(form.createRegister)
