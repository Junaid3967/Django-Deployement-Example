from django.contrib.auth.models import User
from django import forms
from basic_app.models import UserPortfolioInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserPortfolioInfo
        fields = ('portfolio_url', 'profile_pic')