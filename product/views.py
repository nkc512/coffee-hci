from django.http import HttpResponse
from data.models import Blend,Batch,TasteProfile
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import Http404
from data.views import fun,ag

def index(request):
    return HttpResponse("<h1>this is the data home</h1>")

class HomeView(TemplateView):
    template_name= 'product/Home.html'

    def get(self, request):
        blends = Blend.objects.all()
        return render(request,self.template_name,{'blends':blends})

def all_blend(request):
    obj = Blend.objects.all()
    context ={
        'Objects': obj,
    }
    return render(request,"data/all.html",context)

def simple_view(request):

    return render(request,"data/home.html")

def detail_view(request,Blend_id):
    try:
        blend = Blend.objects.get(pk=Blend_id)
        p = list(Batch.objects.filter(blend=Blend_id).values_list('id', flat=True))
        pic = TasteProfile()
        for i in p:
            if TasteProfile.objects.filter(blend_batch_id=i).exists():
                pic = TasteProfile.objects.get(blend_batch_id=i)
    except Blend.DoesNotExist:
       raise Http404("Blend Does not exist")
    return render(request, "product/detail.html", {'blend': blend, 'pic': pic})

def taste_profile_view(request,Blend_id):
    try:
        p = Batch.objects.filter(blend=Blend_id).values_list('id', flat=True)
        print(p)
        pic=TasteProfile.objects.all()
        print(pic)
    except Blend.DoesNotExist:
       raise Http404("Taste Profile Does not exist")
    return render(request, "product/taste_profile.html", {'batch':p,'pic': pic})

