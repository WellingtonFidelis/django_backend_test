from rest_framework import serializers
from .models import FormTest

class FormTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTest
        fields = ['id', 'first_name', 'last_name', 'birth_date']
