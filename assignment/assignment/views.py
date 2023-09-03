from django.http import JsonResponse
from .models import Array
from .serializers import ArraySerializer
import random

from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view




@api_view(['GET'])
def array_generator(request):
    '''get all the drinks
        serialize them
        return json
    '''
    if request.method == 'GET':
        serializer = ArraySerializer(data = request.data)
        if serializer.is_valid():
            if len(request.data['sentence'].split()) > 1: 
                serializer.save()
                vector = [random.uniform(0, 1) for _ in range(500)]

                response_data = {
                    'sentence': request.data['sentence'],
                    'array': vector
                }
                return Response(response_data, status = status.HTTP_200_OK)
            else:
                Response({'error': 'Input is not a sentence'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)