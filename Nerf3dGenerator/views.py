import os
import subprocess

from rest_framework.response import Response
from rest_framework import status

from .funcs import extract_frames_from_video, train_scene_model
from .serializers import  UnitSerializer,DimensionSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST', 'PUT', 'DELETE'])
def generate_Dataset(request):

    try:
        serializer = unitSerializer(data=request.data)
        output_dir=os.path.join(os.getcwd(), 'Nerf3dGenerator/Dataset/')
        if serializer.is_valid():
            # Check if the output folder already exists and remove it
            if os.path.exists(output_dir):
                subprocess.run(['rm', '-r', output_dir])

            # Create the output folder
            os.makedirs(output_dir)

            # Extract the video from the request
            video_data = request.data.get('video')
            if not video_data:
                return Response({'error': 'Video not found'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            # Create a Dataset of Video Frames
            extract_frames_from_video(str(video_data).replace(" ","_"),output_dir)

            # success
            response_data = serializer.data
            response_data['status'] = 'SUCCESS'

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST', 'PUT', 'DELETE'])
def generate_3d_model(request):

    try:
        serializer = DimensionSerializer(data=request.data)
        output_dir=os.path.join(os.getcwd(), 'Nerf3dGenerator/Dataset/')

        if serializer.is_valid():

            # Extract the video from the request
            video_data = request.data.get('videoPath')
            if not video_data:
                return Response({'error': 'Video not found'}, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            #Train the Video Frames Scene
            train_scene_model(str(video_data).replace(" ","_"),output_dir)

            # success
            response_data = serializer.data
            response_data['status'] = 'SUCCESS'

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
