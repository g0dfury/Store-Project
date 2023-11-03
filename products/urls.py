
from django.urls import path
from . import views     # importing views from the current folder



urlpatterns = [
    path('products/', views.ViewAllProducts.as_view()),
    path('products/<int:product_id>/', views.ProductDetails.as_view()),    
    path('products/category/<int:category_id>/', views.ViewProductsByCategory.as_view()), 
]


