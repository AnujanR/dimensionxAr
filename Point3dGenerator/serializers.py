from rest_framework import serializers
from .models import Image_WBG, Dimensioned_Model


class unitSerializer(serializers.ModelSerializer):

    class Meta:
        model=Image_WBG
        fields=['uploadDate','uploadTime','image','status']

class DimensionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Dimensioned_Model
        fields=['uploadDate','uploadTime','imgPath','status']


