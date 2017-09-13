from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def homePage(request):
  if request.method == 'POST':
    Item.objects.create(text=request.POST['itemText'])
    return redirect('/')
  items = Item.objects.all()
  return render(request, 'lists/home.html', {'items': items})
