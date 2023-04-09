from django.shortcuts import render

# Create your views here.
def home(requests):
    return render (requests, "home/index.html")


def shop(requests):
    return render (requests, "shop/index.html")