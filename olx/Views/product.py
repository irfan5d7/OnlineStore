from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from olx.Views import show_category
from olx.forms import *
from olx.models import Category, Product
import datetime
#
# def add_product(request,category_name_slug):
#     template_name = 'add_product.html'
#     try:
#         category = Category.objects.get(slug = category_name_slug)
#     except Category.DoesNotExist:
#         category = None
#     form = ProductForm()
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             if category :
#                 product = form.save(commit = False)
#                 product.category = category
#                 product.seller= request.user
#                 product.posted_on = product.sold_on = datetime.date.today()
#                 import ipdb
#                 ipdb.set_trace()
#                 product.save()
#                 return show_category(request,category_name_slug)
#         else :
#             print(form.errors)
#     context_dict = {'form':form,'category':category}
#     return render(request,'add_product.html',context_dict)
#

class CreateProductView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Product
    form_class = AddProduct
    template_name = 'add_product.html'
    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        return context
    def post(self, request, *args, **kwargs):
        product_form = AddProduct(request.POST,request.FILES)
        if product_form.is_valid():
            product = product_form.save(commit = False)
            category = Category.objects.get(slug=kwargs.get('category_name_slug'))
            product.category = category
            product.seller = request.user
            product.posted_on = product.sold_on =  datetime.date.today()
            product.save()
        return redirect('olx:index')

class UpdateProductView(LoginRequiredMixin,UpdateView):
   login_url = '/login/'
   model = Product
   form_class = AddProduct
   template_name = 'add_product.html'
   def get_success_url(self):
       return reverse('olx:index')
   def get_context_data(self, **kwargs):
       context = super(UpdateProductView, self).get_context_data(**kwargs)
       return context
   def post(self, request, *args, **kwargs):
       product = Product.objects.get(id = kwargs.get('pk'))
       form = AddProduct(request.POST,instance=product)
       form.save()
       return redirect('olx:index')


class DeleteProductView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Product
    success_url = reverse_lazy('olx:myPosts')
    def get_success_url(self):
        return reverse('olx:myPosts')
    def get(self, request, *args, **kwargs):
        return self.post(request, args, kwargs)
    def post(self, request, *args, **kwargs):
        self.delete(request,args,kwargs)
        return redirect('olx:myPosts')

