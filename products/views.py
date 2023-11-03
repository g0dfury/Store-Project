from django.shortcuts import render
from django.views import View # importing View
from .models import * # importing our models
from django.http import HttpResponse # importing HttpResponse

class ViewAllProducts(View):        
    def get(self, request):
        products = Product.objects.all()    
        context = {
            'title': 'Список продуктов',
            'products': products,
        }
        return render(request, 'products/index.html', context=context)
        


class ProductDetails(View):
    def get(self, request, product_id): 
        try:         
            products = Product.objects.get(id=product_id)
        except:
            return HttpResponse('Product not found')

        context = {
            'title': 'Описание продукта',
            'product': products
        }

        return render(request, 'products/details.html', context=context)


class ViewProductsByCategory(View):
    def get(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category)

            context = {
                'title': f'Товары в категории {category.name}',
                'products': products
            }

            return render(request, 'products/category.html', context=context)
        except Category.DoesNotExist:
            return HttpResponse('Category not found')
