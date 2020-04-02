from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Profile_Review,Gen_Review,TasteProfile,Profile,Batch,Blend,Item
from django.views.generic import ListView, DetailView

import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from django.db.models import Avg

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Order,OrderItem,Item
def pltfun(i,values,N,categories):
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    ax = plt.figure(figsize=(5, 5))
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=10)
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3, 4, 5], ["1", "2", "3", "4", "5"], color="grey", size=10)
    plt.ylim(0, 5)

    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    pth = str(i)
    pthimg = "gallery/"+pth+".png"
    pth = str("media/gallery/" + pth + ".png")
    plt.savefig(pth)
    t = TasteProfile()
    if TasteProfile.objects.filter(blend_batch_id=i).exists():
        t = TasteProfile.objects.get(blend_batch_id=i)
    t.blend_batch_id = i
    t.Img = pthimg
    t.save()
    plt.close()


def fun():
    df = pd.DataFrame(list(Profile.objects.all().values()))
    print(df)
    s=list(df['blend_batch_id'])
    df=df.drop(columns=['blend_batch_id','id'])
    print(df)
    a = df[:2]
    categories = list(a)[:10]
    N = len(categories)
    count=0
    for i in s:
        values = df.loc[count].values.flatten().tolist()
        values = values[:10]
        values += values[:1]
        pltfun(i,values,N,categories)
        count=count+1



def index(request):
    ag()
    fun()
    obj = TasteProfile.objects.all()

    context = {
        'BatchPicImage': obj,

    }
    return render(request, "data/picdisplay.html", context)

def ag():
    p = Batch.objects.values_list('id',flat=True)
    s = Profile()
    f = ['acidic','sweet','salty', 'floral', 'chocolaty', 'nutty','bitter','savoury', 'spicy', 'berries']
    for a in p:
        x = []
        for i in f:

            #x.append(Profile_Review.objects.filter(blend_Batch_Id=a).aggregate(Avg(i)))
            l=Profile_Review.objects.filter(blend_batch_id=a).aggregate(Avg(i))
            g=str(i+'__avg')
            x.append(l[g])

        if Profile.objects.filter(blend_batch_id=a).exists():
            s = Profile.objects.get(blend_batch_id=a)
        s.blend_batch_id = a
        s.acidic = x[0]
        s.berries = x[1]
        s.bitter = x[2]
        s.chocolaty = x[3]
        s.floral = x[4]
        s.nutty = x[5]
        s.salty = x[6]
        s.savoury = x[7]
        s.spicy = x[8]
        s.sweet = x[9]

        s.save()

def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    return render(request, "item_list.html",context)

class P_ReviewCreate(CreateView):
    model = Profile_Review
    fields = ['blend_batch_id','user_id','acidic','sweet','salty', 'floral',
              'chocolaty', 'nutty','bitter','savoury', 'spicy', 'berries']

class G_ReviewCreate(CreateView):
    model = Gen_Review
    fields = ['estate_batch', 'review']

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request,"base.html",context)

def checkout(request):
    return render(request,"checkout.html")




class HomeView(ListView):
    model = Item
    template_name="base.html"
class ItemDetailView(DetailView):
    model=Item
    template_name="/product/detail.html"
def add_to_cart(request, slug):
    item=get_object_or_404(Item,slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs=Order.objects.Filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity=1
            order_item.save()
    else:
        order=Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect("core:product",kwargs={
        'slug':slug
    })