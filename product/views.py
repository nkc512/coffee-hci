from django.http import HttpResponse
from data.models import Blend,Batch,TasteProfile
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import Http404
from data.views import fun,ag

def index(request):
    return HttpResponse("<h1>this is the data home</h1>")

class HomeView(TemplateView):
    template_name= 'product/home.html'

    def get(self, request):
        bnd = Blend.objects.all()
        return render(request,self.template_name,{'bnd':bnd})

def all_blend(request):
    ag()
    fun()
    obj = Blend.objects.all()
    context ={
        'Objects': obj,
    }
    return render(request,"product/all.html",context)

def simple_view(request):

    return render(request,"product/Home.html")

def detail_view(request,Blend_id):
    ag()
    fun()
    try:
        blend = Blend.objects.get(pk=Blend_id)
        p = list(Batch.objects.filter(Blend=Blend_id).values_list('id', flat=True))
        pic = TasteProfile()
        for i in p:
            if TasteProfile.objects.filter(Blend_Batch_id=i).exists():
                pic = TasteProfile.objects.get(Blend_Batch_id=i)
    except Blend.DoesNotExist:
       raise Http404("Blend Does not exist")
    return render(request, "product/detail.html", {'blend': blend, 'pic': pic})

def tp_view(request,Blend_id):
    try:
        p = Batch.objects.filter(Blend=Blend_id).values_list('id', flat=True)
        print(p)
        pic=TasteProfile.objects.all()
        print(pic)
    except Blend.DoesNotExist:
       raise Http404("Taste Profile Does not exist")
    return render(request, "product/taste_profile.html", {'batch':p,'pic': pic})

