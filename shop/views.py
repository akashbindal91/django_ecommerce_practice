from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    text = 'This is the first page.'
    return HttpResponse(text)