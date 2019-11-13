from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form, 'title': 'Register'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account Profile has Updated! Please login Again!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': request.user.username.title() + '\'s Profile'
    }
    return render(request, 'user/profile.html', context)


def change_password(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm(data=request.POST, user=request.user)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, f'Your Password has Updated!')
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
    context = {
        'pass_change_form': pass_change_form,
        'title': request.user.username.title() + '\'s Profile'
    }
    return render(request, 'user/change_password_form.html', context)