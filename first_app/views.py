from django.shortcuts import render
from django.http import HttpResponse

from .models import Topic
from .forms import SearchForm, TestForm
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def app_index(request):
    favorite_book = {'Raymond': "The Kite Runner", 'Emma': "A Thousand Splendid Suns",
                     'Denise': "The Great Gatsby", 'Austin': "Holly Lover"}
    return render(request, 'first_app/index.html', context=favorite_book)
    # return HttpResponse("Hello from my first app!")


def home(request):
    try:
        # user = User.objects.create_user(
        #     username="Kotomi", email="123@gmail.com", password="123")
        # user.save()
        topic = Topic.objects.create(top_name="Songs")
        topic.save()
    except IntegrityError as e:
        print(e)
    return HttpResponse("Welcome to the home page of my first app!")


def show_age(request, age):
    return HttpResponse(f"I am {age} years old.")


def odd_or_even(request, num):
    if (num % 2 == 0):
        result = "even"
    else:
        result = "odd"
    return HttpResponse(f"{num} is an {result} number!")


def forms(request):
    form = SearchForm()
    return render(request, 'first_app/form.html', {'form': form})


def test_forms(request):
    test_form = TestForm()
    return render(request, "first_app/form.html", {'form': test_form})


def handle_forms(request):
    form = TestForm(request.POST or None)
    data = "None"
    text = None
    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
    return render(request, 'first_app/form.html', {'form': form, 'data': data, 'text': text})


def modify_user(request):
    try:
        user = User.objects.get(username="Kotomi")
        user.email = "456@gmail.com"
        user.save()
    except IntegrityError as e:
        print(e)
    return HttpResponse("Welcome to modify user page!")
