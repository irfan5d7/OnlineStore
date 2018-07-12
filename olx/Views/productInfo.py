from django.shortcuts import render

from olx.models import Product, Comments, UserProfile


def product_info(request,pk):
    product = Product.objects.get(id=pk)
    if product.seller != request.user and product.is_sold == False:
        product.views=product.views+1
        product.save()
    try:
        comments = Comments.objects.filter(product__id = pk).values('comments','user__username')
        context_dict ={}
        context_dict['product'] = product
        context_dict['comm'] = comments
        profile = UserProfile.objects.filter(user__username=request.user.username)
        if profile:
            profile = profile[0]
        context_dict['prof'] = profile
    except:
        pass
    return render(request,'productInfo.html',context_dict)