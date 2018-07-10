from django.shortcuts import render

from olx.models import Product, Comments


def product_info(request,pk):
    product = Product.objects.get(id=pk)
    if product.seller != request.user and product.is_sold == False:
        product.views=product.views+1
        product.save()
    comments = Comments.objects.filter(product__id = pk).values('comments','user__username')

    context_dict ={}
    context_dict['product'] = product
    context_dict['comm'] = comments
    return render(request,'productInfo.html',context_dict)