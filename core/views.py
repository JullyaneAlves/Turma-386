from django.shortcuts import render

# Create your views here.
# mysite/core/views.py


from django.http import HttpResponse

def home(request):
    return HttpResponse("Alô Mundo!")
