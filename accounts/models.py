# accounts/models.py

#from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
    # ... fields ...

# id : PK
# username 
# first_name
# last_name
# email
# password
# is_staff
# is_activate
# is_superuser
# last_login
# data_joined