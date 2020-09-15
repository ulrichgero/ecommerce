from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    DetailView,
    UpdateView,
    CreateView
)
from .models import Product, Category

#get product into the home page



class ProductList(ListView):
    model = Product
    paginate_by = 8


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProducCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'category', 'image', 'price', 'short_desc', 'full_desc', 'price', 'avaliable']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'category', 'image', 'price', 'short_desc', 'full_desc', 'price', 'avaliable']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        product = self.get_object()
        if self.request.user == product.author:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = 'product'

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False

class CategoryDetail(DetailView):
    model = Category
    template_name = 'product/category.html'

    def get_queryset(self):
        return Category.objects.filter(name__icontains='fashion')


#categories views

class CategoryList(ListView):
    model = Category
    paginate_by = 12 

    def get_queryset(self):
        return Category.objects.all().filter()
    

def allprod(request):
    product = Product.objects.all()
    context = {'product' : product}
    return render(request, 'home.html', context=context)


def category_list(request):
    category = Category.objects.all()
    context = { 'category' : category}
    return render(request, 'product_list.html', context=context )