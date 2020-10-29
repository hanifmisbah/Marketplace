from django.forms import ModelForm
from django.forms import ClearableFileInput
from . import models

class Toko(ModelForm):
	class Meta:
		model=models.Toko
		exclude=[]
	
	# def __init__(self, *args, **kwargs):
	# 	super(Toko, self).__init__(*args, **kwargs)
	# 	self.fields['pemilik'].widget.attrs['class'] = 'form-control'
	# 	self.fields['nama'].widget.attrs['class'] = 'form-control'
	# 	self.fields['alamat'].widget.attrs['class'] = 'form-control'
	# 	self.fields['telp'].widget.attrs['class'] = 'form-control'
	# 	self.fields['gambar'].widget.attrs['class'] = 'form-control'
