from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from products.models import Product

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products'] = context['product_list']

        #print(context)
        return context
    
class ProductDetailView(DetailView): # busqueda mediante id
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        

        print(context)
        return context
