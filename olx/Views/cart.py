import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView

from olx.models import *

class ShowCartView(LoginRequiredMixin,ListView):
        login_url = '/login/'
        model = Cart
        template_name = 'cart.html'
        def get_context_data(self, **kwargs):
            context = super(ShowCartView, self).get_context_data(**kwargs)
            # cart = Cart.objects.filter(user__id=self.request.user.id, product__is_sold=False).values('id', 'product__id',
            #                                                                                     'product__name',
            #                                                                                     'product__price',
            #                                                                                     'product__seller__username',
            #                                                                                     'product__image',
            #                                                                                     'product__is_sold')
            cart = Cart.objects.filter(user=self.request.user)
            context.update({
                'products': cart,
                'user_permissions': self.request.user.get_all_permissions()
            })
            return context

#
# def show_cart(request):
#     context_dict = {}
#     try:
#         cart = Cart.objects.filter(user__id=request.user.id ,product__is_sold= False).values('id','product__id','product__name','product__price','product__seller__username','product__image','product__is_sold')
#         context_dict['products'] = cart
#     except Cart.DoesNotExist:
#         pass
#     return render(request, 'cart.html', context_dict)

def buy(request,pk):
    context_dict = {}
    product = Product.objects.get(id = pk)
    product.is_sold = True
    product.posted_on = datetime.date.today()
    product.buyer = request.user.username
    product.save()
    car = Cart.objects.get_or_create(product=product,user=request.user)
    return redirect('olx:myOrders')

def myOrders(request):
    context_dict = {}
    try:
        cart = Cart.objects.filter( user=request.user,product__is_sold=True)
        context_dict['products'] = cart
    except Cart.DoesNotExist:
        pass
    return render(request, 'myOrders.html', context_dict)
def my_posts(request):
    context_dict = {}
    try:
        product = Product.objects.filter(seller_id = request.user.id)
        context_dict['products'] = product
    except Cart.DoesNotExist:
        pass
    return render(request, 'myPosts.html', context_dict)

def add_toCart(request,pk):
    context_dict = {}
    product = Product.objects.get(id=pk)
    cart = Cart(user=request.user,product=product)
    cart.save()
    return redirect('olx:cart')


def remove_from_cart(request,pk):
    Cart.objects.filter(id = pk).delete()
    return redirect('olx:cart')


def return_product(request,pk):
    cart = Cart.objects.filter(product__id = pk).delete()
    product = Product.objects.get(id = pk)
    product.is_sold = False
    product.buyer = ''
    # product.sold_on = product.posted_on
    product.save()
    return redirect('olx:cart')
