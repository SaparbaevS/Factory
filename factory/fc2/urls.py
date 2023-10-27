from django.urls import path, re_path
from . import views

app_name = 'factory2'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    re_path(r'^product/(?P<product_id>\d+)/$', views.product_detail, name='product_detail1'),
]