from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from olx.models import Category, UserProfile, Product



class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        context = super(CategoryListView,self).get_context_data(**kwargs)
        category_list = Category.objects.all()
        profile = UserProfile.objects.filter(user__username=self.request.user.username)
        product = Product.objects.all().order_by('-posted_on')[0:6]
        prod_views = Product.objects.exclude(is_sold=True).order_by('-views').exclude()
        if profile:
            profile=profile[0]
        prod = Product.objects.all()
        context.update({
            'categories': category_list,
            'prof':profile,
            'product':product,
            'prod_view':prod_views,
            'user_permissions': self.request.user.get_all_permissions()
        })
        return context
