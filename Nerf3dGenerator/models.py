from django.db import models

class Video_WBG(models.Model):
    uploadDate = models.DateField(auto_now=True)
    uploadTime = models.TimeField(auto_now=True)
    video = models.FileField(upload_to='Nerf3dGenerator/Dataset/')
    status = models.CharField(max_length=25, default="FAILED")


class Dimensioned_Model(models.Model):
    uploadDate = models.DateField(auto_now=True)
    uploadTime = models.TimeField(auto_now=True)
    videoPath = models.CharField(max_length=265)
    status = models.CharField(max_length=25, default="FAILED")