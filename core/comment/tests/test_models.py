from django.test import TestCase
from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment

# Create your tests here.

def test_create_comment(user, post):
    comment = Comment.objects.create(author=user, post=post, body="test comment body")
    assert comment.body == "test comment body"
    assert comment.author == user
    assert comment.post == post