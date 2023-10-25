from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from Products.models import Product
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestProductRetrieveTests:
    url = reverse('product-list')

    def test_product_list_return_200_status(self, api_client):
        product = Product.objects.create(name='test case 1', details='test case details', price=5.00)
        response = api_client.get(f'{self.url}{product.pk}/') 
        assert response.status_code == status.HTTP_200_OK



@pytest.mark.django_db
class TestProductCreateTests:
    url = reverse('product-list')

    def test_create_product_valid_return_200_status(self, api_client):
        product_data = {'name': "test case 2", "details": "test case 2 details", "price": 80.9}
        response = api_client.post(self.url, product_data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_product_invalid_return_404_status(self, api_client):
        product_data = {'name': "", "details": "test case 2 details", "price": "80.9"}
        response = api_client.post(self.url, product_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST