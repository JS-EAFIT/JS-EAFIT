from django.contrib import admin
from django.urls import path
from django.shortcuts import render

def comprador(request):
    return render(request, 'comprador.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comprador/', comprador, name='comprador'),
]
