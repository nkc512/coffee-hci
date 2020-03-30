from django.conf.urls import url
from django.urls import path
from . import views
import re

urlpatterns = [
    path('home/', views.simple_view, name='home'),
    url(r'^tp/(?P<Blend_id>[0-9]+)/', views.tp_view, name='tp'),
    url(r'^(?P<Blend_id>[0-9]+)/', views.detail_view, name='detail'),
    url(r'all/', views.all_blend, name='all'),
]