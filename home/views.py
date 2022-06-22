from django.shortcuts import render
from django.http import HttpResponse
from mymusic import templates

# Create your views here.
def render_homepage(request):
    return render(request,'home.html')
