from django.db import models
from django.contrib.auth.models import AbstractUser

    # find the diff between null and blank
class MyUserClass(models.Model):
    username = None
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    USERNAME_FIELD = "email"    

    def __str__(self):
        return str("{} {}".format(self.first_name, self.last_name))

