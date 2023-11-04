from django import forms # importing forms
from django.contrib.auth.models import User # importing User (from admin panel)
from django.contrib.auth.forms import UserCreationForm


# class UserSignUpForm(forms.Form):
#     username = forms.CharField(label='Имя пользователя', 
#     widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})) # виджет внутри формочки
#     email = forms.EmailField(label='Укажите вашу почту')
#     first_name = forms.CharField(required=False, label='Ваше имя')
#     last_name = forms.CharField(required=False, label='Ваша фамилия')
#     password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput())

class UserSignUpForm(UserCreationForm):
    # description = forms.CharField() -> добавление поля
    class Meta: 
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'passwrod1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }