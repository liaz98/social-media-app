from conftest import client
from core.fixtures.user import user
from rest_framework import status

class TestUserViewSet:
    endpoint = '/api/user/'

    def test_client(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
    
    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        response=client.get(self.endpoint + str(user.public_id)+ "/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["username"] == user.username
        assert response.data["email"] == user.email
        assert response.data["first_name"] == user.first_name
        assert response.data["last_name"] == user.last_name
    
    def test_create(self, client, user):
        client.force_authenticate(user=user)
        data={
            "username": "test2",
            "password": "test2",
            "email": "test2@mail.com",
            "first_name": "test2",
            "last_name": "test2",
        }
        response = client.post(self.endpoint, data)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    
    def test_update(self, client, user):
        client.force_authenticate(user=user)
        data={
            "first_name": "test2",
            "last_name": "test2",
        }
        response = client.patch(self.endpoint + str(user.public_id)+"/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["first_name"] == data["first_name"]
        assert response.data["last_name"] == data["last_name"]
        
