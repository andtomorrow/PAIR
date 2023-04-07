# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            birthday=form.cleaned_data.get('birthday')
            user=authenticate(username=username, password=raw_password)
            user.birthday=birthday
            user.save()
            auth_login(request,user)
            return redirect('posts:index')
    else:
        form=CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html',context)

@login_required
def delete(request):
    request.user.delete()
    return redirect('posts:index')

from django.contrib import messages
@login_required
def update(request):
    if request.method=='POST':
        form=CustomUserChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            if request.user.check_password(password):
                form.save()
                messages.success(request,'회원정보가 수정되었습니다.')
                #update_session_auth_hash(request,user)
                return redirect('posts:index')
            else:
                messages.error(request,'비밀번호가 일치하지 않습니다.')
    else:
        form=CustomUserChangeForm(instance=request.user)
    context={
        'form':form,
    }
    return render(request,'accounts/update.html',context)

@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user) #암호 변경시 세션 무효화 방지
            return redirect('posts:index')
    else:
        form=PasswordChangeForm(request.user)
    context={
        'form':form,
    }
    return render(request, 'accounts/change_password.html',context)