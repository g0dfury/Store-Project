from django.urls import path
from .views import ProductCreateView

app_name = 'add_product'

urlpatterns = [
    path('', ProductCreateView.as_view(), name='new'),
]