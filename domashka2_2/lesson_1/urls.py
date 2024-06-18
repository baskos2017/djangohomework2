from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lesson_1-index'), 
    path('<str:subpage>/', views.subpage, name='lesson_1-subpage'), 
]
