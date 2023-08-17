from django.test import TestCase
import pytest
from core.user.models import User

# Create your tests here.


data_user = {
    "username": "test",
    "password": "test",
    "email": "test@gmail.com",
    "first_name": "test",
    "last_name": "test",
}

data_superuser ={
    "username": "superuser_test",
    "password": "superuser_test",
    "email": "superuser@mail.com",
    "first_name": "superuser",
    "last_name": "superuser",
}

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.username == data_user["username"]
    assert user.email == data_user["email"]
    assert user.first_name == data_user["first_name"]
    assert user.last_name == data_user["last_name"]


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(**data_superuser)
    assert user.email == data_superuser["email"]
    assert user.username == data_superuser["username"]
    assert user.first_name == data_superuser["first_name"]
    assert user.last_name == data_superuser["last_name"]
    assert user.is_staff == True
    assert user.is_superuser == True
    assert user.is_active == True

