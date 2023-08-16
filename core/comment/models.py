from django.db import models

from core.abstract.models import AbstractManager, AbstractModel

# Create your models here.

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    author = models.ForeignKey("core_user.User", on_delete=models.PROTECT)
    post = models.ForeignKey("core_post.Post", on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    object = CommentManager()

    def __str__(self) -> str:
        return self.author.name

