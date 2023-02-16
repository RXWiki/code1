from django.contrib.auth import login
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
import django.utils.datastructures

from .models import *
from .forms import *
from .utils import *


def questions(request, value):
    quest = get_object_or_404(Questions, pk=value)
    choice = get_object_or_404(Choice, pk=value)
    return render(request, 'museum/questions.html',
                  {'value': value, 'title': "Вопрос ", 'quest': quest, 'choice': choice})


def yes(request,value):
    user_id = request.user.id
    user = Person(borrower_id=user_id)
    user.resultat = user.resultat + 1
    user.save()
    print(user.resultat)
    return render(request, 'museum/questions.html')

def no(request,value):
    user_id = request.user.id
    user = Person(borrower_id=user_id)
    user.resultat = user.resultat
    user.save()
    print(user.resultat)
    return render(request, 'museum/questions.html')

def ready(request):
    return render(request, 'museum/ready.html', {'title': 'Вы готовы?'})


def if_not_found(request, exception):
    return HttpResponseNotFound("<h1>URL not Found</h1>")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'museum/index.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'museum/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('ready')
