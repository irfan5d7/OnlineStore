from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from olx.models import Product


def get_product_list(max_results = 0,starts_with = ''):
    product_list = []
    if starts_with:
        product_list = Product.objects.filter(name__istartswith=starts_with)
        if max_results > 0:
            if len(product_list) > max_results:
                product_list = product_list[:max_results]
    return product_list

def suggest_product(request):
    product_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
        cat_list = get_product_list(8, starts_with)
    return render(request, 'prod.html', {'prod': cat_list })
