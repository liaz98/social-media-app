from django.test import TestCase
import pytest
from core.fixtures.user import user
from conftest import client
from rest_framework import status

# Create your tests here.


class TestAuthenticationViewSet:
    endpoint = '/api/auth/'

    def test_login(self, client, user):
        data={
            "username":user.username,
            "password":"test"
        }
        response = client.post(self.endpoint + 'login/', data)
        print(response.data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['user']['username'] == user.username
        assert response.data['user']['email'] == user.email
        assert response.data['user']['first_name'] == user.first_name
        assert response.data['user']['last_name'] == user.last_name
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex
    
    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "johndoe",
            "email": "john@mail.com",
            "password": "test_password",
            "first_name": "John",
            "last_name": "Doe"
        }
        response = client.post(self.endpoint + 'register/', data)
        assert response.status_code == status.HTTP_201_CREATED  
    
    def test_refresh(self, client, user):
        data = {
            "username": user.username,
            "password": "test"
        }
        response = client.post(self.endpoint + "login/", data)
        assert response.status_code == status.HTTP_200_OK

        data_refresh = {
            "refresh": response.data['refresh']
        }

        response = client.post(self.endpoint + "refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']