from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404



# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if (request.GET):
        print(request.GET)

    # if (request.POST):
    #     print(request.POST)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

# def categories(request, cat):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True) #301
        # raise ()
        # return redirect('/') # 302
        # return redirect('/', permanent=True) #301
        
    
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")
 


# page404
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')