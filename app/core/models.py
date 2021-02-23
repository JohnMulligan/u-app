from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
PermissionsMixin

class UserManager(BaseUserManager):
    ##**extra_fields is a shortcut, allows def to accept extra arguments
    def create_user(self,email,password=None, **extra_fields):
        ##this function creates and saves a new user
        ##the below instantiates a new "user" sub-class
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

#making a custom model
class User(AbstractBaseUser,PermissionsMixin):
    #custom user model that supports using email instead of username
    email = models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD='email'



# Create your models here.
