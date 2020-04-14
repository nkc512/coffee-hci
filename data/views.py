from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Profile_Review,Gen_Review,TasteProfile,Profile,Batch,Blend,Coffee_Order
from django.views.generic import ListView, DetailView, TemplateView
from django.http import Http404
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from django.db.models import Avg
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#from .models import Order,OrderItem
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
    print(pth)
    plt.savefig(pth)
    t = TasteProfile()
    if TasteProfile.objects.filter(blend_batch_id=i).exists():
        t = TasteProfile.objects.get(blend_batch_id=i)
    t.blend_batch_id = i
    t.img = pthimg
    t.save()



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

def comments(request):
    obj = Gen_Review.objects.all()

    context = {
        'reviews': obj,
    }
    return render(request, "data/reviewdisplay.html", context)


def ag():
    blend_batch_ids = Batch.objects.values_list('id',flat=True)
    
    taste = ['acidic','sweet','salty', 'floral', 'chocolaty', 'nutty','bitter','savoury', 'spicy', 'berries']
    for blend_batch_id in blend_batch_ids:
        x = []
        #if Profile_Review.objects.filter(blend_batch_id=blend_batch_id).exists():
        
        for taste_specific in taste:

            #x.append(Profile_Review.objects.filter(blend_Batch_Id=a).aggregate(Avg(i)))
            l=Profile_Review.objects.filter(blend_batch_id=blend_batch_id).aggregate(Avg(taste_specific))
            #print(l)
            g=str(taste_specific+'__avg')
            x.append(l[g])
        
        print('x',x)
        s=Profile()
        if Profile.objects.filter(blend_batch_id=blend_batch_id).exists():
            s = Profile.objects.get(blend_batch_id=blend_batch_id)
        s.blend_batch_id = blend_batch_id
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
        'items' : Blend.objects.all()
    }
    return render(request, "item_list.html",context)

class P_ReviewCreate(CreateView):
    model = Profile_Review
    fields = ['blend_batch_id','user_id','acidic','sweet','salty', 'floral',
              'chocolaty', 'nutty','bitter','savoury', 'spicy', 'berries']

class G_ReviewCreate(CreateView):
    model = Gen_Review
    fields = ['blend_batch', 'review']

def products(request):
    context = {
        'items': Blend.objects.all()
    }
    return render(request,"data/blend_list.html",context)




class BlendListView(ListView):
    model = Blend
    template_name="data/blend_list.html"
class BlendDetailView(DetailView):
    model=Blend
    template_name="data/blend_detail.html"

'''
def add_to_cart(request, pk):
    item=get_object_or_404(Blend,pk=pk)
    order_item = OrderItem.objects.create(item=item)
    print('add to cart called-----------------------------------------------')
    order_qs=Order.objects.Filter(user=request.user, ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity=1
            order_item.save()
    else:
        order=Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect("/data/add_to_cart",kwargs={
        'pk':item.pk
    })
'''
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
    return render(request, "data/blend_detail.html", {'blend': blend, 'pic': pic})

def taste_profile_view(request,Blend_id):
    try:
        p = Batch.objects.filter(blend=Blend_id).values_list('id', flat=True)
        print(p)
        pic=TasteProfile.objects.all()
        print(pic)
    except Blend.DoesNotExist:
       raise Http404("Taste Profile Does not exist")
    return render(request, "data/taste_profile.html", {'batch':p,'pic': pic})


def add_to_cart(request,Blend_id):
    print(Blend_id)
    blend = get_object_or_404(Blend,pk=Blend_id)
    preexisting_order,created = Coffee_Order.objects.get_or_create(blend=blend)
    print(type(preexisting_order))
    preexisting_order.quantity = preexisting_order.quantity+1
    preexisting_order.save()
    context=create_cart_view()
    return render(request, "data/blend_cart.html",context)

def create_cart_view():
    blend_cart=Coffee_Order.objects.all()
    cartitems=[]
    totalquantity=0
    totalcost=0
    for item in blend_cart:
        temp = get_object_or_404(Blend,pk=item.blend.id)
        cost = temp.price
        itemname = temp.name
        quantity = item.quantity
        totalcost+=cost*quantity
        totalquantity+=quantity
        cartitems.append({'itemname':itemname,'quantity':quantity,'costeach':cost,'costtotal':cost*quantity})

    context = {
        'cart': cartitems,
        'totalcost': totalcost,
        'totalquantity':totalquantity
    }
    return context

def cart_view(request):
    context = create_cart_view()
    return render(request, "data/checkout_page.html",context)

'''def login_view(request):
    return render(request, "data/login.html")'''

'''def register_view(request):
    return render(request, "data/register.html")'''

def checkout(request):
    context=create_cart_view()
    return render(request, "data/checkout_page.html",context)


                           
def remove_from_cart(request,Blend_id):
    blend = get_object_or_404(Blend,pk=Blend_id)
    try:
        preexisting_order = Coffee_Order.objects.get(blend=blend)
        if preexisting_order.quantity > 1:
            preexisting_order.quantity -= 1
            preexisting_order.save()
        else:
            preexisting_order.delete()
    except Coffee_Order.DoesNotExist:
        pass   

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('/'))

def register_view(request):
    print('reach 1------------------------------------------')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        print('reach 2------------------------------------------')
        if user_form.is_valid():
            print('reach 3 -----------------------')
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'data/register.html',
                          {'user_form':user_form,
                           'registered':registered})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'data/login.html', {})