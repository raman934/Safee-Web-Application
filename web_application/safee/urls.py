from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
	path('', PostListView.as_view(), name = 'safee'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('about/', views.about, name = 'safee-about'),
	path('index/', views.index, name = 'safee-home'),
	path('generic/', views.generic, name = 'safee-generic'),
	path('elements/', views.elements, name = 'safee-elements'),
]
