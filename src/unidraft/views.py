from django.contrib.auth.forms import UsernameField
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "unidraft/index.html")

def about(request):
    return render(request, "unidraft/about.html")


def login(request):
    return render(request, "unidraft/signin.html")


def signup(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            account = authenticate(email=email, password=password)
            return redirect('login')

    context = {'form': form}
    return render(request, "unidraft/signup.html", context)
