
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Profile_Review,Gen_Review,TasteProfile,Profile,Batch

import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from django.db.models import Avg


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
    if TasteProfile.objects.filter(Blend_Batch_id=i).exists():
        t = TasteProfile.objects.get(Blend_Batch_id=i)
    t.Blend_Batch_id = i
    t.Img = pthimg
    t.save()


def fun():
    df = pd.DataFrame(list(Profile.objects.all().values()))
    print(df)
    s=list(df['Blend_Batch_id'])
    df=df.drop(columns=['Blend_Batch_id','id'])
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
    f = ['Acidic','Sweet','Salty', 'Floral', 'Chocolaty', 'Nutty','Bitter','Savoury', 'Spicy', 'Berries']
    for a in p:
        x = []
        for i in f:

            #x.append(Profile_Review.objects.filter(blend_Batch_Id=a).aggregate(Avg(i)))
            l=Profile_Review.objects.filter(blend_Batch_Id=a).aggregate(Avg(i))
            g=str(i+'__avg')
            x.append(l[g])

        if Profile.objects.filter(Blend_Batch_id=a).exists():
            s = Profile.objects.get(Blend_Batch_id=a)
        s.Blend_Batch_id = a
        s.Acidic = x[0]
        s.Berries = x[1]
        s.Bitter = x[2]
        s.Chocolaty = x[3]
        s.Floral = x[4]
        s.Nutty = x[5]
        s.Salty = x[6]
        s.Savoury = x[7]
        s.Spicy = x[8]
        s.Sweet = x[9]

        s.save()

class P_ReviewCreate(CreateView):
    model = Profile_Review
    fields = ['blend_Batch_Id','User_Id','Acidic','Sweet','Salty', 'Floral',
              'Chocolaty', 'Nutty','Bitter','Savoury', 'Spicy', 'Berries']

class G_ReviewCreate(CreateView):
    model = Gen_Review
    fields = ['Estate_Batch', 'review']


