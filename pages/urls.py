from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('results', views.about, name='results'),
    path('results', views.search),
    # path('vodka', views.vodka),
]