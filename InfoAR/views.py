import os

from django.shortcuts import render

from InfoAR.funcs import colorExtractor
from InfoAR.serializers import infoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST', 'PUT', 'DELETE'])
def get_info(request):
    serializer = infoSerializer(data=request.data)

    if serializer.is_valid():
        # Extract the image from the request
        imgPath = request.data.get('imgPath')
        if not imgPath:
            return Response({'error': 'Image not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract Colours From Image
        extractedColors=colorExtractor(imgPath)
        print(extractedColors)
        if not extractedColors:
            return Response({'error': 'Error in Extraction'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer.save()

        # success
        response_data = serializer.data
        response_data['colors']=extractedColors
        response_data['status'] = 'SUCCESS'

        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
