import pytest

from core.user.models import User

data_user = {
    "username": "test",
    "password": "test",
    "email": "test@gmail.com",
    "first_name": "test",
    "last_name": "test",
}

@pytest.fixture
def user(db)-> User:
    return User.objects.create_user(**data_user) 