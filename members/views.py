from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from members.forms import RegisterUserForm, AddTravelForm
from django.views.generic import View
from mysite.models import AddTravel


def index(request, *args, **kwargs):
    return render(request, 'index.html')

def my_messages(request, *args, **kwargs):
    return render(request, 'messages.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("There was an error logging in!"))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('index')



def register_user(request):
    print('FORM DATA')
    if request.method == "POST":
        print('request POST')
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print('FORM IS VALID')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            print(username, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successfull"))
            return redirect('index')
    else:
        print('else request POST')
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form': form})

def myprofile(request):

    return render(request, 'authenticate/myprofile.html', {})


def add_travel_page(request):
       if request.method == "POST":
             form = AddTravelForm(request.POST)
             if form.is_valid():
                 obj = AddTravel()
                 obj.from_where = form.cleaned_data['from_where']
                 obj.to_where = form.cleaned_data['to_where']
                 obj.transport_type = form.cleaned_data['transport_type']
                 obj.how_long_traveled = form.cleaned_data['how_long_traveled']
                 obj.with_whom = form.cleaned_data['with_whom']
                 obj.accommodation = form.cleaned_data['accommodation']
                 obj.reason = form.cleaned_data['reason']
                 obj.money_spent = form.cleaned_data['money_spent']
                 obj.save()

                 messages.success(request, ("Congratulations, You've successfully added ypur trip!"))
                 return redirect('add_travel_page')
       else:
                 form = AddTravelForm()
       return render(request, 'authenticate/add_travel_page.html', {'form': form})

