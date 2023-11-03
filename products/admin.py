from django.contrib import admin
from .models import *       # importing all models
# Register your models here.
# Registation of our models -> 

admin.site.register(Category)
admin.site.register(Product)