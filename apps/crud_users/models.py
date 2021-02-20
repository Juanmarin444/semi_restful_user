from __future__ import unicode_literals
from django.db import models

#Our new manager!
#No methods in our new manager should ever catch the whole
#request object with a parameter!!! (just parts, like request.POST)

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "User's name should be more than 5 characters"
        if len(postData['email']) < 10:
            errors["email"] = "User's email should be more than 10 characters"
        return errors

class User(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 254)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
