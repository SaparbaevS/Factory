from django.shortcuts import render, get_object_or_404
from .models import ConfectioneryFactoryproduct2
from fc1.models import ConfectioneryFactoryproduct1
def product_list(request):
    factory2_products = ConfectioneryFactoryproduct2.objects.all()
    factory1_products = ConfectioneryFactoryproduct1.objects.all()
    return render(request, 'index.html', context={'factory2_products': factory2_products,'factory1_products': factory1_products})

def product_detail(request, product_id):
    product = get_object_or_404(ConfectioneryFactoryproduct2, id=product_id)
    return render(request, 'product_info.html', context={'product': product})
