import os
import subprocess
from io import BytesIO

from rest_framework.response import Response
from rest_framework import status
from PIL import Image
from .funcs import removeBg, generate_point_clouds
from .serializers import unitSerializer, DimensionSerializer
from rest_framework.decorators import api_view
import torch
from tqdm.auto import tqdm
from django.http import FileResponse


@api_view(['POST', 'PUT', 'DELETE'])
def create_alpha_mask(request):
    serializer = unitSerializer(data=request.data)
    output_dir = os.path.join(os.getcwd(), 'Point3dGenerator/Dataset/')

    if serializer.is_valid():
        # Check if the output folder already exists and remove it
        if os.path.exists(output_dir):
            subprocess.run(['rm', '-r', output_dir])

        # Create the output folder
        os.makedirs(output_dir)

        # Extract the image from the request
        image_data = request.data.get('image')
        if not image_data:
            return Response({'error': 'Image not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the image to remove the background and save to dropbox
        img, removed = removeBg(image_data, output_dir)
        if not removed:
            return Response({'error': 'Error in Removing Image'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer.save()

        # success
        response_data = serializer.data
        response_data['imageName'] = str(image_data)
        response_data['status'] = 'SUCCESS'

        return Response(response_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT', 'DELETE'])
def generate_3d_model(request):
    serializer = DimensionSerializer(data=request.data)

    if serializer.is_valid():

        # Get the Continuity Status
        statusR = request.data.get('status')
        if statusR != "SUCCESS":
            return Response({'error': 'User Cancelled The Generation'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            image_name = request.data.get('imageName')
            generate_point_clouds(image_name)

            serializer.save()

            # success
            file_path = 'Point3dGenerator/Dataset/' + str(image_name).split('.')[0] + '.ply';
            response = FileResponse(open(file_path, 'rb'), as_attachment=True,filename=str(image_name).split('.')[0] + '.ply')
            response['status'] = 'SUCCESS'

            return response
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
