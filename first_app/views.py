from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def app_index(request):
    return HttpResponse("Hello from my first app!")


def app_home(request):
    return HttpResponse("Welcome to the home page of my first app!")


def show_age(request, age):
    return HttpResponse(f"I am {age} years old.")


def odd_or_even(request, num):
    if (num % 2 == 0):
        result = "even"
    else:
        result = "odd"
    return HttpResponse(f"{num} is an {result} number!")
