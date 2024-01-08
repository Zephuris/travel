from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm,UpdateProfileForm,ImageUploadForm, UserLoginForm,ChangePasswordForm
from .models import ProfilePic
from dashboard.models import Travel
from dashboard.views import TravelViewSet

@login_required(login_url="/accounts/login/")
def OwnedTravelViewSet(request):
    travel_qs = Travel.objects.filter(tour_lead_id = request.user.id)
    user_qs = User.objects.get(id = request.user.id)
    return render(request=request,template_name='account-dashboard.html',context={'travels':travel_qs,
                                                                                  'user':user_qs})

def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Successfully Registered!!")
            return redirect(TravelViewSet)
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request ,
                   template_name="account-register.html",
                   context={"register_form" : form})

def loginView(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data = request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(TravelViewSet)
            else:
                messages.error(request,"Given Credentials Are INVALID!!")
        else:
            messages.error(request,"Given Credentials Are INVALID!!")
    form = UserLoginForm()
    return render(request , "account-login.html",context={'login_form':form})

def DashbordView(request):
    user_qs = User.objects.get(id = request.user.id)

    return render(request , "account-dashboard.html",context={'user':user_qs})

def ProfileView(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(DashbordView)
    else:
        profile_form = UpdateProfileForm()
    return render(request, "account-profile.html",{'form':profile_form})

def logoutView(request):
    logout(request)
    messages.info(request,'Succussfully Logged out!')
    return redirect(TravelViewSet)

def passwordEditView(request):
    if request == 'POST' :
        form = ChangePasswordForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('passwordEditView')
        messages.error(request,'Invalid Password!')
    form = ChangePasswordForm(request.user)
    return render(request,'account-password.html',context={'form':form})

def ImageAddView(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
    form = ImageUploadForm()
    return render(request,'add-pic.html',context={'form':form})

