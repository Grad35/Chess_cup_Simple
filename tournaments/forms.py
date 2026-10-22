from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="Электронная почта")
    first_name=forms.CharField(label="Имя",max_length=40)
    last_name=forms.CharField(label="Фамилия",max_length=40)
    class Meta:
        model=User
        fields=("username","first_name","last_name","email","password1","password2")
        labels={"username":"Логин"}
