# it converts python object into json   
from rest_framework import serializers
from .models import Array


class ArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Array
        fields = ['id','sentence']
