from rest_framework import serializers
from .models import Video_WBG,Dimensioned_Model

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model=Video_WBG
        fields=['uploadDate','uploadTime','video','status']

class DimensionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Dimensioned_Model
        fields=['uploadDate','uploadTime','videoPath','status']


