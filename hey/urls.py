from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/',views.search_results, name='search_results'),
    path('category/',views.category, name='category'),
    
]


    