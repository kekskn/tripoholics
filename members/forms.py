import attrs as attrs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from mysite.models import AddPastTravel, AddFutureTravel, MyProfile
from datetime import date
from django.forms.widgets import SelectDateWidget
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyProfile
        fields = ('country', 'profile_image')

    def clean_profile_image(self):
        profile_image = self.cleaned_data.get('profile_image')
        if profile_image:
            if profile_image.size > 4 * 1024 * 1024:
                raise ValidationError(_("File size should not exceed 4 MB."))
            if not profile_image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError(_("Only image files are allowed."))
        return profile_image

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if len(country) > 50:
            raise ValidationError(_("Country name should not exceed 50 characters."))
        return country


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


TRANSPORT = (
    ('Plane', 'plane'),
    ('Train', 'train'),
    ('Bus', 'bus'),
    ('Car', 'car'),
    ("Bike", "bike"),
    ("Hitchhike", "hitchhike"),
    ("Ship", "ship"),
    ("Other", "other"),
)

COMPANY = (
    ("Alone", "alone"),
    ("Couple", "couple",),
    ("With friend", "with friend"),
    ("Group of friends", 'group of friends'),
    ("Family", 'family'),
    ("Colleagues (work/college/school)", 'colleagues (work/college/school)'),
)

ACCOMMODATION = (
    ("Hotel", "hotel"),
    ("Hostel", "hostel",),
    ("Camping", "camping"),
    ("Apartments", 'apartments'),
    ("RV", 'RV'),
    ("Friends/family", 'friends/family'),
    ("Hospitality exchange services", 'hospitality exchange services'),
    ("Other", 'other'),
)

REASON = (
    ("Leisure", "leisure"),
    ("Snow and ski", "snow and ski",),
    ("Sun and beach", "sun and beach"),
    ("Event travel", 'event travel'),
    ("Nature travel", 'nature travel'),
    ("Adventure travel", 'adventure travel'),
    ("City break", 'city break'),
    ("Food and wine", 'food and wine'),
    ("Volunteer work", 'volunteer work'),
    ("Business", 'business'),
)

MONEY_SPENT = (
    ("150", "150"),
    ("150-300", "150-300",),
    ("300-500", "300-500"),
    ("500-1000", '500-1000'),
    ("1000-3000", '1000-3000'),
    ("3000+", '3000+'),
)


class PastSelectDateWidget(SelectDateWidget):
    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs['class'] = 'date-select'
        years = range(datetime.date.today().year - 100, date.today().year + 1)
        kwargs['years'] = years
        super().__init__(*args, **kwargs)


class AddPastTravelForm(forms.ModelForm):
    from_where = CountryField().formfield(widget=forms.Select(attrs={'id': 'id_from_where'}))
    to_where = CountryField().formfield(widget=forms.Select(attrs={'id': 'id_to_where'}))
    transport_type = forms.ChoiceField(choices=TRANSPORT, label='Which transportation you have used?',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    when_traveled = forms.DateField(widget=PastSelectDateWidget(attrs={'class': 'form-control'}),
                                    label="When you traveled?",
                                    validators=[MaxValueValidator(limit_value=date.today)])
    how_long_traveled = forms.IntegerField(label="How long this trip lasted?", validators=[MinValueValidator(0)],
                                           widget=forms.NumberInput(attrs={'class': 'form-control'}))
    with_whom = forms.ChoiceField(choices=COMPANY, label='With whom you traveled?',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    accommodation = forms.ChoiceField(choices=ACCOMMODATION, label='Accommodation type',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    reason = forms.ChoiceField(choices=REASON, label="Reason of travel",
                               widget=forms.Select(attrs={'class': 'form-control'}))
    money_spent = forms.ChoiceField(choices=MONEY_SPENT, label='On this trip ypu spent...',
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    pictures = forms.ImageField(allow_empty_file=True, label='Your pictures from your trip', required=False)

    class Meta:
        model = AddPastTravel
        fields = (
            'from_where', 'to_where', 'transport_type', 'when_traveled', 'how_long_traveled', 'with_whom',
            'accommodation',
            'reason', 'money_spent', 'pictures')


class AddFutureTravelForm(forms.ModelForm):
    from_where = CountryField().formfield(widget=forms.Select)
    to_where = CountryField().formfield(widget=forms.Select)
    transport_type = forms.ChoiceField(choices=TRANSPORT, label='Which transportation will you use?',
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    when_traveled = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}),
                                    label="When was your trip planned for?")
    how_long_traveled = forms.IntegerField(label="How long this trip will last?", validators=[MinValueValidator(0)],
                                           widget=forms.NumberInput(attrs={'class': 'form-control'}))
    with_whom = forms.ChoiceField(choices=COMPANY, label='With whom you will travel?',
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    accommodation = forms.ChoiceField(choices=ACCOMMODATION, label='Accommodation type',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    reason = forms.ChoiceField(choices=REASON, label="Reason of travel",
                               widget=forms.Select(attrs={'class': 'form-control'}))
    money_spent = forms.ChoiceField(choices=MONEY_SPENT, label='On this trip you plan to spend...',
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = AddFutureTravel
        fields = (
            'from_where', 'to_where', 'transport_type', 'when_traveled', 'how_long_traveled', 'with_whom',
            'accommodation',
            'reason', 'money_spent')
