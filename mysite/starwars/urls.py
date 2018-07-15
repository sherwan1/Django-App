from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.films, name='films'),
    re_path(r'^characters/(?P<id>[0-9]*)/$', views.characters, name='characters')
    #path(r'^characters/(?P<id>[0-9]*)/$', views.characters, name='characters'),
]