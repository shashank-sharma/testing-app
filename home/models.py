from django.db import models
from django.contrib import admin

# Create your models here.

# Model form for username, address and email id
class Form(models.Model):
    username = models.TextField(max_length = 80, blank = False)
    address = models.TextField(max_length = 200, blank = False)
    email = models.TextField(max_length = 80, blank = False)
