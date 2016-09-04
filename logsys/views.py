from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm


def log_in(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'User not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def log_out(request):
    logout(request)
    return redirect('/')


def sing_up(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreateForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('singup.html', args)
