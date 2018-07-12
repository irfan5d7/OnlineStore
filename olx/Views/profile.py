from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from django.views.generic.base import View

from olx.forms import AddProfile
from olx.models import UserProfile


class ProfileView(View):
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
            'prof':prof
        }
        return render(request,"profile.html",context)

#
# def ProfileView(request,value):
#     profile = UserProfile.objects.filter(user__username=value).values('user__username', 'user__email',
#                                                                                  'address', 'contact_no', 'picture')
#     if profile:
#         profile = profile[0]
#     context = {'prof':profile}
#     # import ipdb
#     # ipdb.set_trace()
#     return render(request, 'profile.html', context)
#


class CreateProfileView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = UserProfile
    form_class = AddProfile
    template_name = 'profile_regis.html'
    def get_context_data(self, **kwargs):
        context = super(CreateProfileView, self).get_context_data(**kwargs)
        return context
    def post(self,request,*args,**kwargs):
        profile_form = AddProfile(request.POST,request.FILES)
        if profile_form.is_valid():
            prof = profile_form.save(commit=False)
            prof.user=self.request.user
            prof.save()
        return redirect('olx:index')


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = UserProfile
    form_class = AddProfile
    template_name = 'profile_regis.html'
    def get_success_url(self):
        return reverse('olx:index')
    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        return context
    def post(self, request, *args, **kwargs):
        prof = UserProfile.objects.get(user = kwargs.get('pk'))
        form = AddProfile(request.POST,request.FILES,instance=prof)
        form.save()
        return redirect('olx:index')
