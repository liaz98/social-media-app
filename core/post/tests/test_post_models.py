from django.test import TestCase
import pytest
from core.fixtures.user import user
from core.post.models import Post

# Create your tests here.

@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="test Post body")
    assert post.body == "test Post body"
    assert post.author == user
