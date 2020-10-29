from django.urls import path
from . import views

urlpatterns = [
	path('', views.index), # ITEMS # ITEMS # ITEMS
	path('input_products/', views.input),
	path('category/', views.category),
	path('category/input_category/', views.input_c),
	path('<id>/delete', views.delete),
	path('category/<id>/delete', views.delete_c),
	path('<id>/update', views.update)
]