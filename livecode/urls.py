from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='Halaman_shop'),
    path('<int:shop_id>/',views.shop_detail, name='shop_detail'),
    path('inputshop/',views.listshop, name='Daftar_toko'),
]
