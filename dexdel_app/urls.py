from django.urls import path
from . import views

urlpatterns = [
    path('',views.tesing),
    path('search.html',views.search),
    # path('search.html/<ask>',views.search,name='anything')
]