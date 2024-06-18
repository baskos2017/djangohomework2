from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home-view'),  # Маршрут для 'home/' з ім'ям 'home-view'
    path('book/<str:title>/', views.book, name='book'),  # Маршрут для 'book/{назва глави}/' з ім'ям 'book'
    path('lesson_2/', include('lesson_2.urls')),  # Перенаправлення запитів, що починаються з 'lesson_2/'
]
