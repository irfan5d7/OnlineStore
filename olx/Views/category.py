from django.shortcuts import render
from django.views.generic import ListView

from olx.models import *


def show_category(request,category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    query = None
    try:
        category = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name
        products = Product.objects.filter(category=category,is_sold=False).exclude(seller__username__exact=request.user.username).order_by('price')
        context_dict['products'] = products
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    if not context_dict['query']:
        context_dict['query'] = category.name
    return render(request, 'category.html', context_dict)


def show_category_price_dec(request,category_name_slug):
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    query = None
    try:
        category = Category.objects.get(slug = category_name_slug)
        context_dict['category_name'] = category.name
        products = Product.objects.filter(category=category,is_sold=False).exclude(seller__username__exact=request.user.username).order_by('-price')
        context_dict['products'] = products
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    if not context_dict['query']:
        context_dict['query'] = category.name
    return render(request, 'category.html', context_dict)
