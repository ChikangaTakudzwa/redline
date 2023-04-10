from django.shortcuts import render

# Create your views here.
def home(requests):
    return render (requests, "home/index.html")

def shop(requests):
    return render (requests, "shop/index.html")

def single_product(requests):
    return render (requests, "shop/single_product.html")

def cart(requests):
    return render (requests, "cart/cart_page.html")

