from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from travelagency.forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from assignmenttwo.settings import AUTH_TOKEN


@login_required
def my_view(request):
    ...


User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1  # 1 == True
    return render(request, "travelagency/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # user is valid and active -> is_active
            # request.user == user
            login(request, user)
            return redirect("/chatbot")
        else:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1  # 1 == True
    return render(request, "travelagency/form.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def hi(request):
    return render(request, 'travelagency/hi.html')


def authenticate_tkn(token):
    if token == AUTH_TOKEN:

        return True

    else:

        return False
