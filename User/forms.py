from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=["email","username"]
        widgets={'email':forms.EmailInput(attrs={'placeholder':"Enter Your Email","required":True,"id":"email"}),"username":forms.TextInput(attrs={'placeholder':"Enter a Username"}),\
                'password1':forms.PasswordInput(attrs={'placeholder':"Enter Password"}),"password2":forms.PasswordInput(attrs={'placeholder':"Re-Enter Password"})}

    consent=forms.BooleanField(label="Do You Agree to Our Terms and Conditions",help_text="Terms and Condition",default=True,required=True)
