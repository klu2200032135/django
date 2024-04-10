from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
import random
import string

from django.template.defaulttags import comment
from requests import auth

from .forms import *

def hello1(request):
    return HttpResponse("<center>Welcome To TTM HomePage</center>")
# Create your views here.
def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method=="POST":
        user_input=request.POST.get('user_input')
        print(f'userinput:{user_input}')
    a1={'user_input':{user_input}}
    return render(request,'print_to_console.html',a1)

def randomcall(request):
    return render(request,'randomotp.html')


def randomcall1(request):
    if request.method=="POST":
        user_input=request.POST.get('user_input')
        print(f'user input:{user_input}')
        a2=int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))
    a1={'ran1':ran1}
    return render(request,'randomotp.html',a1)

def get_date1(request):
    return render(request,'datetime12.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method=='POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'datetime12.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'datetime12.html',{'form':form})


from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.Choose a different email.")
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'myregisterpage.html')
def registerlogin(request):
    return render(request,'myregisterpage.html')

import matplotlib.pyplot as plt
import numpy as np
def piechart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/download.png')  # Save the chart image
            img1={'chart_image': '/static/images/download.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

def pie_chart(request):
    return render(request,'chart_form.html')


def Car(request):
    return render(request,'Car.html')

import requests
def weatherpagecall(request):
    return render(request,'weatherappinput.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'd1c334165bfa2e84c9d048cf6590b242'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})


def login(request):
    return render(request, 'login.html')



def feedbackfunction(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phonenumber = form.cleaned_data['phonenumber']
            comments = form.cleaned_data['comments']
            tosend=comments+'_this is copy of you feedback.'

            # Save feedback data to the database
            feedback = Feedback(name=name, email=email, phonenumber=phonenumber, comments=comments)
            feedback.save()

            send_mail(
                'thank you for concateting siva Travel Tourisam and Mangement System.',
                tosend,
                'sivaganeshyasam@gmailcom',
                [email],
                fail_silently=False,
            )
            # Display a success message
            messages.success(request, 'Feedback submitted successfully.')

            return redirect('/')  # Change 'thank_you_page' to the actual URL or name of your thank you page

        else:
            form = FeedbackForm()

        return render(request, 'contactus.html', {'form': form})
def feedback(request):
    return render(request, 'contactus.html')


def signup(request):
    return render(request, 'signup.html')


def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'NewHomePage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')
def login(request):
    return render(request, 'login.html')
def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'newhomepage.html')