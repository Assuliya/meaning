from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    return render(request, 'meaning_shop/index.html')
