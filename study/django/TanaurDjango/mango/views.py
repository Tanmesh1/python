from django.shortcuts import render

# Create your views here.

def all_mangoes(request):
    return render(request, 'mango/all_mangos.html')