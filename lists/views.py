from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
  return HttpResponse('<html><title>To-Do lists</title></html>')

