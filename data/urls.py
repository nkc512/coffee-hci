from django.conf.urls import url
from . import views

app_name='core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add/p/',views.P_ReviewCreate.as_view(),name='p_review_add'),
    url(r'add/g/', views.G_ReviewCreate.as_view(), name='g_review_add'),
    path('add-to-cart/<slug>',views.add_to_cart,name='add-to-cart')
]