from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from members.forms import RegisterUserForm, AddFutureTravelForm, AddPastTravelForm
from django.views.generic import View
from mysite.models import AddFutureTravel, AddPastTravel
from mysite.models import MyProfile


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
            return redirect('myprofile')
        else:
            messages.success(request, ("There was an error logging in!"))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('login')



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
            return redirect('myprofile')
    else:
        print('else request POST')
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form': form})

def myprofile(request):

    countries_count = AddPastTravel.objects.all().count()
    cities_count = AddPastTravel.objects.all().count()

    data = {"countries_count": countries_count,
            "cities_count": cities_count}
    p = AddFutureTravel.objects.all()
    data["objs"] = p



    return render(request, 'authenticate/myprofile.html', data)

def add_travel_page(request, *args, **kwargs):
    return render(request, 'authenticate/add_travel_page.html')

def add_next_trip(request):
       if request.method == "POST":
             form = AddFutureTravelForm(request.POST)
             if form.is_valid():
                 obj = AddFutureTravel()
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
                 return redirect('add_next_trip')
       else:
                 form = AddFutureTravelForm()
       return render(request, 'authenticate/add_next_trip.html', {'form': form})

def add_past_trip(request):
    if request.method == "POST":
        form = AddPastTravelForm(request.POST)
        if form.is_valid():
            obj = AddPastTravel()
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
            return redirect('add_past_trip')
    else:
        form = AddPastTravelForm()
    return render(request, 'authenticate/add_past_trip.html', {'form': form})

