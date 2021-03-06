"""carteira_de_investimentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include

from .views import (home_page, contact_page)
from carteira.views import (carteira_create_view, carteira_update_view, carteira_delete_view)


urlpatterns = [
    path('carteira/', include('carteira.urls')),
    path('carteira-new/', carteira_create_view),
    path('carteira_update/<str:ticker>', carteira_update_view),
    path('carteira_delete/<str:ticker>', carteira_delete_view),
	path('home/', home_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]
