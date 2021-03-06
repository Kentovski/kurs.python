"""autobase_homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from autobase import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^auto/shopping-cart', views.shopping_cart),
    url(r'^auto/create', views.auto_create),
    url(r'^auto/edit', views.auto_edit),
    url(r'^auto/', views.auto),
    url(r'^manufacturer/create', views.manufacturer_create),
    url(r'^manufacturer/edit', views.manufacturer_edit),
    url(r'^manufacturer/', views.manufacturer),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
