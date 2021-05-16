from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "unidraft/index.html")


def login(request):
    return render(request, "unidraft/login.html")


def signup(request):
    return render(request, "unidraft/signup.html")
