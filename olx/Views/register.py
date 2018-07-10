from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views.generic.base import View

from olx.forms import *


class SignUpController(View):
    def get(self,request):
        form = SignUpForm()
        return render(
            request,
            template_name='register.html',
            context = {'form':form,'title': 'Signup'}
        )
    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = form.cleaned_data
            import ipdb
            ipdb.set_trace()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('olx:profile_details_add')
            return redirect('olx:login')
        else:
            messages.error(request,'Invalid Credentials')

