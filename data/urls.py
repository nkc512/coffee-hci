from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add/p/',views.P_ReviewCreate.as_view(),name='p_review_add'),
    url(r'add/g/', views.G_ReviewCreate.as_view(), name='g_review_add'),
    url(r'add_to_cart/(?P<Blend_id>[0-9]+)/',views.add_to_cart,name='add_to_cart'),
    url(r'remove_from_cart/(?P<Blend_id>[0-9]+)/',views.remove_from_cart,name='remove_from_cart'),
    path('home/', views.simple_view, name='home'),
    url(r'^tp/(?P<Blend_id>[0-9]+)/', views.taste_profile_view, name='taste_profile'),
    url(r'^(?P<Blend_id>[0-9]+)/', views.detail_view, name='detail'),
    url(r'all/', views.all_blend, name='all'),
    url(r'cart/', views.cart_view, name='blend_cart'),
    url(r'checkout/', views.checkout, name='checkout_page'),
    
]