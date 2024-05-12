from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

# Create your views here.
def main(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request=request,
                template_name= 'index.html',
                context=context
                )

def about(request):
    return render(request=request,
                  template_name='about.html')

def contact(request):
    return render(request=request,
                template_name='contact.html')

def blog_list(request):
    return render(request=request,
                template_name='blog_list.html')

def product(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request=request,
                  template_name='product.html',
                  context=context
                  )

def testimonial(request):
    return render(request=request,
                  template_name='testimonial.html')


def product_detail(request, id):
    product = Products.objects.get(id=id)
    context = {
        'product': product
    }
    return render(request=request,
                  template_name='product_detail.html',
                  context=context
                  )

def phone(request):
    phones = Products.objects.filter(tag='phone').order_by('-id')
    context = {
        'phones': phones
    }
    return render(request=request,
                  template_name='phone.html',
                  context=context)

def laptop(request):
    laptops = Products.objects.filter(tag='laptop').order_by('-id')
    context = {
        'laptops': laptops
    }
    return render(request=request,
                  template_name='laptop.html',
                  context=context)

def apliances(request):
    apliances = Products.objects.filter(tag='apliances').order_by('-id')
    context = {
        'apliances': apliances
    }
    return render(request=request,
                  template_name='apliances.html',
                  context=context)