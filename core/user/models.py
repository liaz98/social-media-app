import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from core.post.models import Post
from core.abstract.models import AbstractManager, AbstractModel
# Create your models here.

def user_directory_path(instance, filename):
     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.public_id, filename)

class UserManager(BaseUserManager, AbstractManager):
    def get_object_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return None
    
    def create_user(self, username, email, password=None, **kwargs):
        if  username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError("Users must have a password")
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise TypeError("Superuser must have a password")
        if username is None:
            raise TypeError("Superuser must have a username")
        if email is None:
            raise TypeError("Superuser must have a email")
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    posts_liked = models.ManyToManyField(
        "core_post.Post",
        related_name="liked_by"
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    def like(self, post):
        return self.posts_liked.add(post)
    
    def remove_like(self, post):
        return self.posts_liked.remove(post)
    
    def has_liked(self, post):
        return self.posts_liked.filter(pk=post.pk).exists()

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
