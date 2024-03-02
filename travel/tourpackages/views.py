from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def homepage(request):
    return render(request, 'Homepage.html')

def flights(request):
    return render(request, 'Flights.html')

def travelpackages(request):
    return render(request, 'Travelpackages.html')

def register1(request):
    return render(request, "Register.html")

def login1(request):
    return render(request, "login.html")

def rentcar(request):
    return render(request, "Rentcar.html")

def alllink(request):
    return render(request, "Alllink.html")

import datetime
import time
import calendar


def date1(request):
    datetime_object = datetime.datetime.now()
    s2 = calendar.month(2023, 4)
    s1 = calendar.isleap(2005)

    context = {
        'datetime_object': datetime_object,
        's2': s2,
        's1': s1,
    }
    return render(request, "Datetime123.html", context)

def randomotp(request):
    return render(request, "Randomotp.html")

import random, string
def randomotp1(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = int(input1)
        result_str = ''.join(random.sample(string.digits, input2))
        print(result_str)
        context = {'result_str': result_str}
    return render(request, "Randomotp.html", context)



def getdate1(request):
    return render(request,'get_date.html')

def getdate2(request):
    return render(request,'result.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)

            return render(request, 'get_date.html', {'updated_date': updated_date})
        else:
            form = IntegerDateForm()
        return render(request, 'get_date.html', {'form': form})

def print1(request):
    return render(request, 'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    # return HttpResponse('Form submitted successfully')
    a1= {'user_input':user_input}
    return render(request,'print_to_console.html',a1)


from django.shortcuts import render

def my_view(request):
    # Your view logic here
    show_alert = True  # Set this based on your condition
    return render(request, 'my_template.html', {'show_alert': show_alert})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home1')  # Replace 'home' with the name of your home view or URL
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import login, authenticate

from django.contrib.auth import login as auth_login  # Renaming the login function

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm  # Import your LoginForm from forms.py

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home1')  # Replace 'home' with the name of your home view or URL
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    auth_logout(request)
    return redirect('home1')
