from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import *

from olx.forms.comment import AddComment
from olx.models import Comments, Product, UserProfile


class CreateCommentView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Comments
    form_class = AddComment
    template_name = 'comment.html'
    def get_context_data(self, **kwargs):
        context = super(CreateCommentView, self).get_context_data(**kwargs)
        return context
    def post(self,request,*args,**kwargs):
        comment_form = AddComment(request.POST)
        if comment_form.is_valid():
            comm = comment_form.save(commit=False)
            comm.user=self.request.user
            product = Product.objects.get(id = kwargs.get('pk'))
            comm.product = product
            comm.save()
        return redirect('olx:productInfo' ,pk = kwargs.get('pk'))

