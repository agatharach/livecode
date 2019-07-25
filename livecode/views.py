from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop
from .forms import InputShop 
from django.http import Http404

# Create your views here.
def Home(request):
    shop_=Shop.objects.all()
    return render(request, 'home.html', {'shop':shop_})

def listshop(request):
    if request.method == 'POST':
        form = InputShop(request.POST)
        if form.is_valid():
            post =form.save(commit=False)
            post.save()
            return redirect ('Halaman_shop')
    else:
        form = InputShop()
    return render(request, 'inputshop.html',{'form':form})

def shop_detail(request,shop_id):
    try :
        shop_=Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'shop_detail.html', {'shop':shop_})