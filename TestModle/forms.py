from django import forms

class register(forms.Form):
    password=forms.CharField()
    username=forms.CharField()

class login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserInfoForm(forms.Form):
    name=forms.CharField(max_length=50)
    tele=forms.CharField()
    addr=forms.CharField()