

from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from authors.forms.login_form import LoginForm

from .forms.register_form import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/new_register.html',
                  {'form': form,
                   'form_action': reverse('authors:register_create'),
                   })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))

    return redirect('authors:register')


def login(request):
    form = LoginForm()
    if request.POST:
        ...
    return render(request, 'authors/pages/login_form.html',
                  {'form': form,
                   'form_action': reverse('restaurant:home'),
                   })
