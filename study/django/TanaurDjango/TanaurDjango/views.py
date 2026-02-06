from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World. You are at Tanmesh aur Django Home page")

def about(request):
    return HttpResponse("Hello, World. You are at Tanmesh aur Django About page")

def contact(request):
    return HttpResponse("Hello, World. You are at Tanmesh aur Django contact page")