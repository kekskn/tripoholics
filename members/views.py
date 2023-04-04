import profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from pymongo import collection
from members.forms import RegisterUserForm, AddFutureTravelForm, AddPastTravelForm, ProfilePicForm
from django.views.generic import View
from mysite.models import AddFutureTravel, AddPastTravel, MyProfile
from django.db.models import Sum, Count, Q, Avg


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
    if request.method == 'POST':
        print('request POST')
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None)
        if user_form.is_valid() and profile_form.is_valid():
            print('FORM IS VALID')
            user_form.save()
            profile_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            print(username, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successfull"))
            return redirect('myprofile')
        else:
            print('FORM IS INVALID')
            print(user_form.errors)
            print(profile_form.errors)
    else:
        print('else request POST')
        user_form = RegisterUserForm()
        profile_form = ProfilePicForm()

    return render(request, 'authenticate/register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def update_user(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST, instance=request.user)
        profile_form = ProfilePicForm(request.POST, request.FILES, instance=request.user.myprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, request.user)

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('myprofile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = RegisterUserForm(instance=request.user)
        profile_form = ProfilePicForm(instance=request.user.myprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'authenticate/update_user.html', context)


@login_required
def add_travel_page(request, *args, **kwargs):
    return render(request, 'authenticate/add_travel_page.html')


@login_required
def add_next_trip(request):
    if request.method == "POST":
        form = AddFutureTravelForm(request.POST)
        if form.is_valid():
            obj = AddFutureTravel()
            obj.from_where = form.cleaned_data['from_where']
            obj.to_where = form.cleaned_data['to_where']
            obj.when_traveled = form.cleaned_data['when_traveled']
            obj.transport_type = form.cleaned_data['transport_type']
            obj.how_long_traveled = form.cleaned_data['how_long_traveled']
            obj.with_whom = form.cleaned_data['with_whom']
            obj.accommodation = form.cleaned_data['accommodation']
            obj.reason = form.cleaned_data['reason']
            obj.money_spent = form.cleaned_data['money_spent']
            obj.user = request.user
            obj.save()

            messages.success(request, ("Congratulations, You've successfully added ypur trip!"))
            return redirect('add_next_trip')
    else:
        form = AddFutureTravelForm()
    return render(request, 'authenticate/add_next_trip.html', {'form': form})


@login_required
def add_past_trip(request):
    if request.method == "POST":
        form = AddPastTravelForm(request.POST)
        if form.is_valid():
            obj = AddPastTravel()
            obj.from_where = form.cleaned_data['from_where']
            obj.to_where = form.cleaned_data['to_where']
            obj.when_traveled = form.cleaned_data['when_traveled']
            obj.transport_type = form.cleaned_data['transport_type']
            obj.how_long_traveled = form.cleaned_data['how_long_traveled']
            obj.with_whom = form.cleaned_data['with_whom']
            obj.accommodation = form.cleaned_data['accommodation']
            obj.reason = form.cleaned_data['reason']
            obj.money_spent = form.cleaned_data['money_spent']
            obj.user = request.user
            obj.save()

            messages.success(request, ("Congratulations, You've successfully added ypur trip!"))
            return redirect('add_past_trip')
    else:
        form = AddPastTravelForm()
    return render(request, 'authenticate/add_past_trip.html', {'form': form})


def map_money_spent(value):
    if value == '150':
        return 150
    elif value == '150-300':
        return 225
    elif value == '300-500':
        return 400
    elif value == '500-1000':
        return 750
    elif value == '1000-3000':
        return 2000
    elif value == '3000+':
        return 3500
    else:
        return 0  # or raise an error, depending on your needs


@login_required
def myprofile(request):
    profile = MyProfile.objects.get(user=request.user.id)

    travel_objects = AddPastTravel.objects.filter(user=request.user)
    unique_countries = set(obj.to_where for obj in travel_objects)
    countries_count = len(unique_countries)
    trip_count = AddPastTravel.objects.filter(user=request.user).count()
    # countries_count = AddPastTravel.objects.filter(user=request.user).values('to_where').count()
    cities_count = len(unique_countries)
    countries_names = list(set([travel.to_where for travel in AddPastTravel.objects.filter(user=request.user)]))
    countries_percent = round((countries_count / 195) * 100, 1)
    stroke_percent = 505 - 505 * countries_percent / 100
    days_total = AddPastTravel.objects.filter(user=request.user).aggregate(Sum('how_long_traveled'))[
        'how_long_traveled__sum']
    if days_total is not None:
        months_on_travel = days_total // 30
    else:
        months_on_travel = 0  # or any other default value

    if months_on_travel and days_total is not None:
        weeks_on_travel = (days_total - months_on_travel * 30) // 7
    else:
        weeks_on_travel = 0  # or any other default value

    if months_on_travel and days_total and weeks_on_travel is not None:
        days_on_travel = (days_total - months_on_travel * 30 - weeks_on_travel * 7)
    else:
        days_on_travel = 0  # or any other default value

    # transport preferences
    plane_percent = int(AddPastTravel.objects.filter(transport_type='Plane', user=request.user).count())
    train_percent = int(AddPastTravel.objects.filter(transport_type='Train', user=request.user).count())
    bus_percent = int(AddPastTravel.objects.filter(transport_type='Bus', user=request.user).count())
    car_percent = int(AddPastTravel.objects.filter(transport_type='Car', user=request.user).count())
    bike_percent = int(AddPastTravel.objects.filter(transport_type='Bike', user=request.user).count())
    hitchhike_percent = int(AddPastTravel.objects.filter(transport_type='Hitchhike', user=request.user).count())
    ship_percent = int(AddPastTravel.objects.filter(transport_type='Ship', user=request.user).count())
    other_percent = int(AddPastTravel.objects.filter(transport_type='Other', user=request.user).count())
    transport_list = [plane_percent, train_percent, bus_percent, car_percent, bike_percent, hitchhike_percent,
                      ship_percent, other_percent]
    # traveled with
    alone_percent = int(AddPastTravel.objects.filter(with_whom='Alone', user=request.user).count())
    couple_percent = int(AddPastTravel.objects.filter(with_whom='Couple', user=request.user).count())
    friend_percent = int(AddPastTravel.objects.filter(with_whom='With friend', user=request.user).count())
    group_percent = int(AddPastTravel.objects.filter(with_whom='Group of friends', user=request.user).count())
    family_percent = int(AddPastTravel.objects.filter(with_whom='Family', user=request.user).count())
    colleague_percent = int(
        AddPastTravel.objects.filter(with_whom='Colleagues (work/college/school)', user=request.user).count())
    travel_list = [alone_percent, couple_percent, friend_percent, group_percent, family_percent, colleague_percent]

    # average trip
    average_trip = AddPastTravel.objects.filter(user=request.user).aggregate(Avg('how_long_traveled'))[
        'how_long_traveled__avg']
    if average_trip is not None:
        rounded_average = round(average_trip, 1)
    else:
        rounded_average = 0  # or any other default value

    # accommodation preferences
    hotel_percent = int(AddPastTravel.objects.filter(accommodation='Hotel', user=request.user).count())
    hostel_percent = int(AddPastTravel.objects.filter(accommodation='Hostel', user=request.user).count())
    camping_percent = int(AddPastTravel.objects.filter(accommodation='Camping', user=request.user).count())
    apartments_percent = int(AddPastTravel.objects.filter(accommodation='Apartments', user=request.user).count())
    RV_percent = int(AddPastTravel.objects.filter(accommodation='RV', user=request.user).count())
    friends_percent = int(AddPastTravel.objects.filter(accommodation='Friends/family', user=request.user).count())
    HES_percent = int(
        AddPastTravel.objects.filter(accommodation='Hospitality exchange services', user=request.user).count())
    otherAP_percent = int(AddPastTravel.objects.filter(accommodation='Other', user=request.user).count())
    accommodation_list = [hotel_percent, hostel_percent, camping_percent, apartments_percent, RV_percent,
                          friends_percent,
                          HES_percent, otherAP_percent]

    # calculate average trip cost
    past_travels = AddPastTravel.objects.filter(user=request.user).exclude(money_spent="")
    money_spent_values = [map_money_spent(travel.money_spent) for travel in past_travels]
    if money_spent_values:
        average_cost = sum(money_spent_values) / len(money_spent_values)
        rounded_avg_cost = round(average_cost, 1)
    else:
        rounded_avg_cost = 0  # or any other default value
    # profile list
    profiles = MyProfile.objects.exclude(user=request.user)
    data = {"countries_count": countries_count,
            "cities_count": cities_count,
            "countries_percent": countries_percent,
            "stroke_percent": stroke_percent,
            "countries_names": countries_names,
            "months_on_travel": months_on_travel,
            "days_on_travel": days_on_travel,
            "days_total": days_total,
            "weeks_on_travel": weeks_on_travel,
            "transport_list": transport_list,
            "travel_list": travel_list,
            "rounded_average": rounded_average,
            "profile": profile,
            "trip_count": trip_count,
            "accommodation_list": accommodation_list,
            "rounded_avg_cost": rounded_avg_cost,
            }
    p = AddFutureTravel.objects.filter(user=request.user).all()
    data["objs"] = p

    return render(request, 'authenticate/myprofile.html', data)
