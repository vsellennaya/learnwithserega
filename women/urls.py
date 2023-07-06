from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'), #http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),


    # path('cats/<int:catid>/', categories), #http://127.0.0.1:8000/cats/1/
    # # path('cats/<slug:cat>/', categories), #http://127.0.0.1:8000/cats/1ss-s_/

    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]