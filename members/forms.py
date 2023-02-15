import attrs as attrs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from mysite.models import AddTravel


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'country', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

TRANSPORT = (
    ("1", "plane"),
    ("2", "train",),
    ("3", "bus"),
    ("4", 'car'),
    ("5", 'bike'),
    ("6", 'hitchhike'),
    ("7", 'ship'),
    ("8", 'other'),
)

COMPANY = (
    ("1", "alone"),
    ("2", "couple",),
    ("3", "with friend"),
    ("4", 'group of friends'),
    ("5", 'family'),
    ("6", 'colleagues (work/college/school)'),
)

ACCOMMODATION = (
    ("1", "hotel"),
    ("2", "hostel",),
    ("3", "camping"),
    ("4", 'apartments'),
    ("5", 'RV'),
    ("6", 'friends/family'),
    ("7", 'hospitality exchange services'),
    ("8", 'other'),
)

REASON = (
    ("1", "leisure"),
    ("2", "snow and ski",),
    ("3", "sun and beach"),
    ("4", 'event travel'),
    ("5", 'nature travel'),
    ("6", 'adventure travel'),
    ("7", 'city break'),
    ("8", 'food and wine'),
    ("9", 'volunteer work'),
    ("10", 'business'),
)

MONEY_SPENT = (
    ("1", "150"),
    ("2", "150-300",),
    ("3", "300-500"),
    ("4", '500-1000'),
    ("5", '1000-3000'),
    ("6", '3000+'),
)


class AddTravelForm(forms.ModelForm):
    from_where = forms.CharField(label='From where you traveled?', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    to_where = forms.CharField(label='Where you traveled?', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transport_type = forms.ChoiceField(choices= TRANSPORT, label='Which transportation you have used?', widget=forms.Select(attrs={'class': 'form-control'}))
    when_traveled = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), label="When you traveled?")
    how_long_traveled = forms.IntegerField(label="How long this trip lasted?", validators=[MinValueValidator(0)], widget=forms.NumberInput(attrs={'class': 'form-control'}))
    with_whom = forms.ChoiceField(choices=COMPANY, label='With whom you traveled?', widget=forms.Select(attrs={'class': 'form-control'}))
    accommodation = forms.ChoiceField(choices=ACCOMMODATION, label='Accommodation type', widget=forms.Select(attrs={'class': 'form-control'}))
    reason = forms.ChoiceField(choices=REASON, label="Reason of travel", widget=forms.Select(attrs={'class': 'form-control'}))
    money_spent = forms.ChoiceField(choices=MONEY_SPENT, label='On this trip ypu spent...', widget=forms.Select(attrs={'class': 'form-control'}))
    pictures = forms.ImageField(allow_empty_file=True, label='Your pictures from your trip', required=False)

    class Meta:
        model = AddTravel
        fields = ('from_where', 'to_where', 'transport_type', 'when_traveled', 'how_long_traveled', 'with_whom', 'accommodation', 'reason', 'money_spent', 'pictures')

   # def save(self):
    #    data = self.cleaned_data
        #addtravel = AddTravel(from_where=data['from_where'], to_where=data['to_where'], transport_type=data['transport_type'], when_traveled=data['when_traveled'], how_long_traveled=data['how_long_traveled'], with_whom=data['with_whom'], accommodation=data['accommodation'], reason=data['reason'], money_spent=data['money_spent'])
     #   fields = ('from_where', 'to_where', 'transport_type', 'when_traveled', 'how_long_traveled', 'with_whom', 'accommodation', 'reason', 'money_spent', 'pictures')


