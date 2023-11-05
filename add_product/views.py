from django.views import View
from django.shortcuts import render, redirect
from .forms import UserAddForm
from products.models import Category, Product
from django.http import HttpResponse
from django.urls import reverse_lazy
# Create your views here.

class ProductCreateView(View):
    def get(self, request):
        form = UserAddForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories
        }

        return render(request, 'add_product/index.html', context=context)

    def post(self, request):

        form = UserAddForm(request.POST)
        if form.is_valid():
            new_product = form.save()
            return redirect(reverse_lazy('products:index'))
        else:
            return HttpResponse('Произошла ошибка в валидации формы', status=400)


