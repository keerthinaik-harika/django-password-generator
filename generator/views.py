from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    #if length is not found in request default 12 will be selected
    length = int(request.GET.get('length',12))

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()_+-')
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    password = ''
    for x in range(length):
        password += random.choice(characters)
    return render(request,'generator/password.html',{'password':password})