import profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse
from pymongo import collection
from members.forms import RegisterUserForm, AddFutureTravelForm, AddPastTravelForm, ProfilePicForm
from django.views.generic import View
from mysite.models import AddFutureTravel, AddPastTravel, MyProfile, Follow
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
    print('myprofile', request.user)
    unique_countries = set(obj.to_where for obj in travel_objects)
    countries_count = len(unique_countries)
    trip_count = AddPastTravel.objects.filter(user=request.user).count()
    # countries_count = AddPastTravel.objects.filter(user=request.user).values('to_where').count()
    cities_count = len(unique_countries)
    countries_names = list(set([travel.to_where for travel in AddPastTravel.objects.filter(user=request.user)]))
    countries_percent = round((countries_count / 195) * 100, 1)
    stroke_percent = 505 - 505 * countries_percent / 100

    days_total_result = AddPastTravel.objects.filter(user=request.user).aggregate(Sum('how_long_traveled'))
    days_total = days_total_result['how_long_traveled__sum'] or 0
    months_on_travel, remainder = divmod(days_total, 30)
    weeks_on_travel, days_on_travel = divmod(remainder, 7)

    # transport preferences
    transport_types = ['Plane', 'Train', 'Bus', 'Car', 'Bike', 'Hitchhike', 'Ship', 'Other']
    transport_dict = {}
    for trans_type in transport_types:
        transport_dict[trans_type] = AddPastTravel.objects.filter(transport_type=trans_type, user=request.user).count()

    transport_list = [int(transport_dict[trans_type]) for trans_type in
                      transport_types]

    # traveled with
    travel_list = list(AddPastTravel.objects.filter(user=request.user)
                       .values('with_whom')
                       .annotate(with_whom_count=Count('with_whom'))
                       .order_by('with_whom')
                       .values_list('with_whom_count', flat=True))
    # average trip
    average_trip = AddPastTravel.objects.filter(user=request.user).aggregate(Avg('how_long_traveled'))[
        'how_long_traveled__avg']
    if average_trip is not None:
        rounded_average = round(average_trip, 1)
    else:
        rounded_average = 0  # or any other default value

    # accommodation preferences
    accommodations = ['Hotel', 'Hostel', 'Camping', 'Apartments', 'RV', 'Friends/family',
                      'Hospitality exchange services', 'Other']
    accommodation_dict = {}
    for accom_type in accommodations:
        accommodation_dict[accom_type] = AddPastTravel.objects.filter(accommodation=accom_type,
                                                                      user=request.user).count()
    accommodation_list = [int(accommodation_dict[accom_type]) for accom_type in
                          accommodations]

    # calculate average trip cost
    past_travels = AddPastTravel.objects.filter(user=request.user).exclude(money_spent="")
    money_spent_values = [map_money_spent(travel.money_spent) for travel in past_travels]
    if money_spent_values:
        average_cost = sum(money_spent_values) / len(money_spent_values)
        rounded_avg_cost = round(average_cost, 1)
    else:
        rounded_avg_cost = 0  # or any other default value

    # reasons of travel
    top_reasons = AddPastTravel.objects.values('reason').annotate(count=Count('id')).order_by('-count')[:3]

    font_sizes = ['2.5rem', '2rem', '1rem']

    result = []

    for i, r in enumerate(top_reasons):
        result.append({
            'reason': r['reason'],
            'count': r['count'],
            'size': font_sizes[i],
        })

    # top_reasons = AddPastTravel.objects.values('reason').annotate(count=Count('id')).order_by('-count')[:3]

    user = request.user
    friends = [following.following for following in request.user.myprofile.following.all()]

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
            "top_reasons": result,
            'user': user,
            'friends': friends,
            }
    p = AddFutureTravel.objects.filter(user=request.user).all()
    data["objs"] = p

    return render(request, 'authenticate/myprofile.html', data)


@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    query = request.GET.get('q')
    if query:
        users = users.filter(username__icontains=query)
    my_profile = request.user.myprofile
    friends = my_profile.friends.all()
    following_profiles = [follow.following for follow in my_profile.following.all()]
    following_usernames = [profile.user.username for profile in following_profiles]
    context = {'users': users, 'friends': friends, 'following_profiles': following_profiles,
               'following_usernames': following_usernames}
    return render(request, 'authenticate/user_list.html', context)


@login_required
def follow(request, pk):
    following_profile = MyProfile.objects.get(pk=pk)
    follow, created = Follow.objects.get_or_create(follower=request.user.myprofile, following=following_profile)
    if not created:
        follow.delete()
    return HttpResponseRedirect(reverse('user_list'))


@login_required
def unfollow(request, profile_pk):
    # check whether the request is coming from my_profile or user_list
    referring_url = request.META.get('HTTP_REFERER')
    print("referring URL:", referring_url)
    try:
        if referring_url == 'http://127.0.0.1:8000/members/users/':
            print('unfollowing from user_list')
            # unfollowing from user_list
            following_profile = MyProfile.objects.get(pk=profile_pk)
            follow = Follow.objects.get(follower=request.user.myprofile, following=following_profile)
        else:
            # unfollowing from my_profile
            print('unfollowing from my_friends')
            following_profile = MyProfile.objects.get(pk=profile_pk)
            follow = Follow.objects.get(follower=request.user.myprofile, following=following_profile)
        print("Follow object:", follow)
        follow.delete()
    except Follow.DoesNotExist:
        raise Http404("Follow does not exist")
    if referring_url == 'http://127.0.0.1:8000/members/users/':
        return HttpResponseRedirect(reverse('user_list'))
    else:
        return HttpResponseRedirect(reverse('my_friends'))


@login_required
def my_friends(request):
    try:
        my_profile = request.user.myprofile
        friends = my_profile.following.all()
        print(friends)
    except MyProfile.DoesNotExist:
        friends = []
    return render(request, 'authenticate/my_friends.html', {'friends': friends})


@login_required
def profile_detail(request, user_id):
    profile = MyProfile.objects.get(user=user_id)

    travel_objects = AddPastTravel.objects.filter(user=user_id)
    unique_countries = set(obj.to_where for obj in travel_objects)
    countries_count = len(unique_countries)
    trip_count = AddPastTravel.objects.filter(user=user_id).count()
    # countries_count = AddPastTravel.objects.filter(user=request.user).values('to_where').count()
    cities_count = len(unique_countries)
    countries_names = list(set([travel.to_where for travel in AddPastTravel.objects.filter(user=user_id)]))
    countries_percent = round((countries_count / 195) * 100, 1)
    stroke_percent = 505 - 505 * countries_percent / 100

    days_total_result = AddPastTravel.objects.filter(user=user_id).aggregate(Sum('how_long_traveled'))
    days_total = days_total_result['how_long_traveled__sum'] or 0
    months_on_travel, remainder = divmod(days_total, 30)
    weeks_on_travel, days_on_travel = divmod(remainder, 7)

    # transport preferences
    transport_types = ['Plane', 'Train', 'Bus', 'Car', 'Bike', 'Hitchhike', 'Ship', 'Other']
    transport_dict = {}
    for trans_type in transport_types:
        transport_dict[trans_type] = AddPastTravel.objects.filter(transport_type=trans_type, user=user_id).count()

    transport_list = [int(transport_dict[trans_type]) for trans_type in
                      transport_types]

    # traveled with
    travel_list = list(AddPastTravel.objects.filter(user=user_id)
                       .values('with_whom')
                       .annotate(with_whom_count=Count('with_whom'))
                       .order_by('with_whom')
                       .values_list('with_whom_count', flat=True))
    # average trip
    average_trip = AddPastTravel.objects.filter(user=user_id).aggregate(Avg('how_long_traveled'))[
        'how_long_traveled__avg']
    if average_trip is not None:
        rounded_average = round(average_trip, 1)
    else:
        rounded_average = 0  # or any other default value

    # accommodation preferences
    accommodations = ['Hotel', 'Hostel', 'Camping', 'Apartments', 'RV', 'Friends/family',
                      'Hospitality exchange services', 'Other']
    accommodation_dict = {}
    for accom_type in accommodations:
        accommodation_dict[accom_type] = AddPastTravel.objects.filter(accommodation=accom_type,
                                                                      user=user_id).count()
    accommodation_list = [int(accommodation_dict[accom_type]) for accom_type in
                          accommodations]

    # calculate average trip cost
    past_travels = AddPastTravel.objects.filter(user=user_id).exclude(money_spent="")
    money_spent_values = [map_money_spent(travel.money_spent) for travel in past_travels]
    if money_spent_values:
        average_cost = sum(money_spent_values) / len(money_spent_values)
        rounded_avg_cost = round(average_cost, 1)
    else:
        rounded_avg_cost = 0  # or any other default value

    # reasons of travel
    top_reasons = AddPastTravel.objects.values('reason').annotate(count=Count('id')).order_by('-count')[:3]
    font_sizes = ['2.5rem', '2rem', '1rem']

    result = [{'reason': r['reason'], 'count': r['count'], 'size': fs} for r, fs in zip(top_reasons, font_sizes)]

    # top_reasons = AddPastTravel.objects.values('reason').annotate(count=Count('id')).order_by('-count')[:3]

    user = request.user
    friends = [following.following for following in request.user.myprofile.following.all()]

    # profile list
    profiles = MyProfile.objects.exclude(user=user_id)
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
            "top_reasons": result,
            'user': user,
            'friends': friends,
            }
    p = AddFutureTravel.objects.filter(user=user_id).all()
    data["objs"] = p

    return render(request, 'authenticate/profile_detail.html', data)
