from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.db.models.fields.files import ImageFieldFile
# Create your models here.
class Toko(models.Model):
    pemilik = models.CharField(default='', max_length=20)
    nama = models.CharField(default='', max_length=20)
    alamat = models.CharField(default='', max_length=100)
    telp = models.CharField(default='',max_length=15)
    gambar = models.TextField(default='')