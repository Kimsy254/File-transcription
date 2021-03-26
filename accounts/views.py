from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from accounts.forms import UserForm,ClientProfileForm,WorkerProfileForm,ClientProfileUpdateForm,WorkerProfileUpdateForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from accounts import models
from accounts.models import Worker,Client
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q


# For Client Sign Up
def ClientSignUp(request):
    user_type = 'client'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        client_profile_form = ClientProfileForm(data = request.POST)

        if user_form.is_valid() and client_profile_form.is_valid():

            user = user_form.save()
            user.is_client = True
            user.save()

            profile = client_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,client_profile_form.errors)
    else:
        user_form = UserForm()
        client_profile_form = ClientProfileForm()

    return render(request,'accounts/client_signup.html',{'user_form':user_form,'client_profile_form':client_profile_form,'registered':registered,'user_type':user_type})


###  For Worker Sign Up
def WorkerSignUp(request):
    user_type = 'worker'
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        worker_profile_form = WorkerProfileForm(data = request.POST)

        if user_form.is_valid() and worker_profile_form.is_valid():

            user = user_form.save()
            user.is_worker = True
            user.save()

            profile = worker_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors,worker_profile_form.errors)
    else:
        user_form = UserForm()
        worker_profile_form = WorkerProfileForm()

    return render(request,'accounts/worker_signup.html',{'user_form':user_form,'worker_profile_form':worker_profile_form,'registered':registered,'user_type':user_type})

## Sign Up page which will ask whether you are client or worker.
def SignUp(request):
    return render(request,'accounts/signup.html',{})

## login view.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html',{})

## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

## User Profile of worker.
class WorkerDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "worker"
    model = models.Worker
    template_name = 'accounts/worker_detail_page.html'

## User Profile for client.
class ClientDetailView(LoginRequiredMixin,DetailView):
    context_object_name = "client"
    model = models.Client
    template_name = 'accounts/client_detail_page.html'

## Profile update for workers.
@login_required
def WorkerUpdateView(request,pk):
    profile_updated = False
    worker = get_object_or_404(models.Worker,pk=pk)
    if request.method == "POST":
        form = WorkerProfileUpdateForm(request.POST,instance=worker)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'worker_profile_pic' in request.FILES:
                profile.worker_profile_pic = request.FILES['worker_profile_pic']
            profile.save()
            profile_updated = True
    else:
        form = WorkerProfileUpdateForm(request.POST or None,instance=worker)
    return render(request,'accounts/worker_update_page.html',{'profile_updated':profile_updated,'form':form})

## Profile update for clients.
@login_required
def ClientUpdateView(request,pk):
    profile_updated = False
    client = get_object_or_404(models.Client,pk=pk)
    if request.method == "POST":
        form = ClientProfileUpdateForm(request.POST,instance=client)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'client_profile_pic' in request.FILES:
                profile.client_profile_pic = request.FILES['client_profile_pic']
            profile.save()
            profile_updated = True
    else:
        form = ClientProfileUpdateForm(request.POST or None,instance=client)
    return render(request,'accounts/client_update_page.html',{'profile_updated':profile_updated,'form':form})



class ClassWorkersListView(LoginRequiredMixin,DetailView):
    model = models.Client
    template_name = "accounts/class_workers_list.html"
    context_object_name = "client"



##################################################################################################

## For changing password.
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed")
            return redirect('home')
        else:
            return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request,'accounts/change_password.html',args)

