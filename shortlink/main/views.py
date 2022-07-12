from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
import pyshorteners
from links.forms import CutLink
from links.models import Links
from main.forms import RegisterUserForm, AuthUserForm


def main_page(request):
    form = CutLink()
    return render(request, 'main/index.html', {'form': form})


def profile_page(request):
    record = Links.objects.filter(user_name__contains=request.user.username).order_by('-time_create')
    return render(request, 'main/profile.html', {'record': record})


def cut_url(request):
    if request.method == 'POST':
        form = CutLink(request.POST)
        if request.user.is_authenticated and form.is_valid():
            shortener = pyshorteners.Shortener()
            cut_link = shortener.tinyurl.short(form.cleaned_data['fullLink'])
            tempform = Links()
            tempform.shortLink = cut_link
            tempform.user_name = request.user.username
            tempform.save()
            return render(request, 'main/shorturl.html', {'tempform': tempform})

        else:
            return redirect('home')


def login_view(request):
    return render(request, 'main/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class AuthUser(LoginView):
    form_class = AuthUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
