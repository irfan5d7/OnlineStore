import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from olx.models import *

class ShowCartView(LoginRequiredMixin,ListView):
        login_url = '/login/'
        model = Cart
        template_name = 'cart.html'
        def get_context_data(self, **kwargs):
            context = super(ShowCartView, self).get_context_data(**kwargs)
            cart = Cart.objects.filter(user=self.request.user)
            profile = UserProfile.objects.filter(user__username=self.request.user.username)
            if profile:
                profile=profile[0]
            context.update({
                'products': cart,
                'prof':profile,
                'user_permissions': self.request.user.get_all_permissions()
            })
            return context


def buy(request,pk):
    context_dict = {}
    product = Product.objects.get(id = pk)
    product.is_sold = True
    product.posted_on = datetime.date.today()
    product.buyer = request.user.username
    product.save()
    car = Cart.objects.get_or_create(product=product,user=request.user)
    return redirect('olx:myOrders')


class buy_view(View):
    login_url = '/login/'
    model = UserProfile
    def get(self, request, *args, **kwargs):
        try:

            profile = UserProfile.objects.get(user__username =kwargs.get('value'))
            prof = UserProfile.objects.filter(user__username=self.request.user.username)
            if prof:
                prof = prof[0]

        except:
            return redirect('olx:profile_details_add')
        context = {
            'profil': profile,
            'prof':prof,
            'prod_id':kwargs.get('pk')
        }
        return render(request,"confirm_buy.html",context)


def myOrders(request):
    context_dict = {}
    try:
        cart = Cart.objects.filter( user=request.user,product__is_sold=True)
        context_dict['products'] = cart
        profile = UserProfile.objects.filter(user__username=request.user.username)
        if profile:
            profile = profile[0]
        context_dict['prof'] = profile
    except Cart.DoesNotExist:
        pass
    return render(request, 'myOrders.html', context_dict)


def my_posts(request):
    context_dict = {}
    try:
        product = Product.objects.filter(seller_id = request.user.id)
        context_dict['products'] = product
        profile = UserProfile.objects.filter(user__username=request.user.username)
        if profile:
            profile = profile[0]
        context_dict['prof'] = profile
    except Cart.DoesNotExist:
        pass
    return render(request, 'myPosts.html', context_dict)

def add_toCart(request,pk):
    context_dict = {}
    product = Product.objects.get(id=pk)
    try:
        cart = Cart.objects.get(user=request.user,product=product)
    except:
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
