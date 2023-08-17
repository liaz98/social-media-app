import pytest


@pytest.fixture
def comment(db, user, post):
    from core.comment.models import Comment
    return Comment.objects.create(author=user, post=post, body="test Comment body")