from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.db.models.fields.files import ImageFieldFile
# import PIL.Image


# Create your models here.
class Cate(models.Model):
	# (( OWNER AKAN AKTIF APABILA SUDAH TERDAPAT FITUR LOGIN ))
	# owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='kategori') 
	name_c = models.CharField(default='', max_length=30)

	def __str__(self):
		return self.name_c	

class Prod(models.Model):
	# owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name='products')  
	cate = models.ForeignKey(Cate, on_delete=models.CASCADE, related_name='termasuk')
	kode = models.CharField(max_length=10)
	name = models.CharField(max_length=30)
	price = models.PositiveIntegerField(default=0)
	stok = models.PositiveSmallIntegerField(default=0)
	image = models.TextField(default='')



# 	def __repr__(self):
# 		return self.cate

# 	def __str__(self):
# 		return self.name

# 	def stok1(self):
# 		return self.name.stok-self.qty


class Units(models.Model):
	name = models.TextField(default='')
