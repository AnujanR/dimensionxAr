from rest_framework import serializers
from .models import  Info_Model


class infoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Info_Model
        fields=['uploadDate','uploadTime','imgPath','status']
