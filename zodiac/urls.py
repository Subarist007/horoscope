"""zodiac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from horoscope.views import index, about, contacts

urlpatterns = [
    path('admin/', admin.site.urls), # Страница админа
    path('', index, name='index'), # Главная страница
    path('about/', about, name='about'), # Страница О проекте
    path('contacts/', contacts, name='contacts'), # Страница Контакты
    path('login/', include('users.urls'), name='login'), # Страница входа\регистрации
    path('<zodiac_sign>/', include('horoscope.urls'), name='horoscope'), # Страница гороскопа для выбранного знака
]
