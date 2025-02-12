from django.shortcuts import render

def comprador(request):
    return render(request, 'comprador.html')  # SIN "perfiles/"
