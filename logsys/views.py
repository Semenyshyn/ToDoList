from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render_to_response
from django.template.context_processors import csrf
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
    return redirect('/auth/login')


def sing_up(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreateForm()
    if request.POST:
        newuser_form = UserCreateForm(request.POST)
        if newuser_form.is_valid():
            user = newuser_form.save()
            user.set_password(request.POST['password2'])
            user.save()
            username = request.POST['username']
            password = request.POST['password2']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('singup.html', args)
