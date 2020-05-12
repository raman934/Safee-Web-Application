from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'safee'),
	path('about/', views.about, name = 'safee-about'),
	path('index/', views.index, name = 'safee-home'),
	path('generic/', views.generic, name = 'safee-generic'),
	path('elements/', views.elements, name = 'safee-elements'),
]
