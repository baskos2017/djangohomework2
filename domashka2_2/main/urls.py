from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index-view'),  
    path('bio/<str:username>/', views.bio, name='bio'),  
]
