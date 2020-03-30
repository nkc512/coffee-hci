from django.http import HttpResponse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from data.models import Blend
from django.urls import reverse_lazy
def index(request):
    return HttpResponse("<h1>this is the data home</h1>")
