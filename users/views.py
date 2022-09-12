from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .forms import RegistrationsForm, LoginForm, ProfileForm
from django.contrib.auth import login, logout, authenticate


class ProfileView(UpdateView):
    template_name = 'profile.html'


def logout_view(request):
    logout(request)
    return redirect('pages:home')


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            raise ValidationError('Неверный номер телефона или пароль!')

    return render(request, 'login.html', context={
        'form': form,
    })


def user_registration(request):
    form = RegistrationsForm()

    if request.method == 'POST':
        form = RegistrationsForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('user:login')

    return render(request, 'registrations.html', context={
        'form': form,
    })
