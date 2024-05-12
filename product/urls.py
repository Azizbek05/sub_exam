from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('blog-list/', blog_list, name='blog_list'),
    path('product/', product, name='product'),
    path('testimonial/', testimonial, name='testimonial'),
    path('product-detail/<int:id>', product_detail, name='product_detail'),
    path('phone', phone, name='phone'),
    path('laptop', laptop, name='laptop'),
    path('apliances', apliances, name='apliances')
]
