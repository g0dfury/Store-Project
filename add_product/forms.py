from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from products.models import Product

class UserAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')
