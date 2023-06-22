from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

# Create your views here.

menu = [{'title': "О сайте", 'url_name': 'about'}, 
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request): #HttpRequest
    posts = Women.objects.all()
    context = {
        'posts': posts, 
        'menu': menu, 
        'title': 'Главная страница' 
        }
    
    return render(request, 'women/index.html', context=context)

def about(request): #HttpRequest
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})

def addpage(request): #HttpRequest
    return HttpResponse('Добавление статьи')

def contact(request): #HttpRequest
    return HttpResponse('Обратная связь')

def login(request): #HttpRequest
    return HttpResponse('Авторизация')



# page404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')