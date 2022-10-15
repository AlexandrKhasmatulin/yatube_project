from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр slug из path()
def group_posts (request, slug):
    return HttpResponse(f'посты в группах {slug}') 
