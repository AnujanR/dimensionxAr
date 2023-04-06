from django.db import models

# Create your models here.
class Image_WBG(models.Model):
    uploadDate = models.DateField(auto_now=True)
    uploadTime = models.TimeField(auto_now=True)
    image = models.ImageField(upload_to='Point3dGenerator/Dataset/')
    status = models.CharField(max_length=25, default="FAILED")


class Dimensioned_Model(models.Model):
    uploadDate = models.DateField(auto_now=True)
    uploadTime = models.TimeField(auto_now=True)
    imgPath = models.CharField(max_length=265)
    status = models.CharField(max_length=25, default="FAILED")
