from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lesson_2-index'),
    path('<str:subpage>/', views.subpage, name='lesson_2-subpage'),
]
