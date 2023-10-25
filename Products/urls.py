from django.urls import path
from .views import Documentation, ProductList, ProductDetail

# URL pattern to VIEW, CREATE the products - [http://...../products]
# UPDATE, DELETE the products - [http://.../products/1]

urlpatterns = [
    path('', Documentation.as_view(), name='documentation'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
