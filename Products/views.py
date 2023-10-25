from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer

class Documentation(TemplateView):
    template_name = 'documentation.html'

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @method_decorator(cache_page(20))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
