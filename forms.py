#-*- coding: utf-8 -*-
import datetime

from django import forms
from django.forms.widgets import Textarea, NumberInput, ChoiceWidget, TextInput, \
         EmailInput, FileInput, PasswordInput


from myapp.widgets import CustomTextArea, CustomCheckBox, CustomChoiceBox
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
    	'username',
        'email',
    	'password']
##############################################################################################################

class LoginForm(forms.Form):
#    username = forms.CharField(max_length=200)
    email_id = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_message(self):
        email = self.data.get('email_id')
        dbuser = self.objects.filter(email_id=email)

        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return email


class FinancePeerJsonForm(forms.Form):
    email_id = forms.EmailField(max_length=150)
    #JsonData = forms.JSONField()
    JsonFile = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class FinancePeerDetailsForm(forms.Form):
    FP_ID     = forms.IntegerField()
    FP_UserID = forms.IntegerField()
    FP_Title  = forms.CharField(max_length=150)
    FP_Body   = forms.Textarea()



