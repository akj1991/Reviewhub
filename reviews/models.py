from django.db import models
import email

class Registration(models.Model):
    fullname = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    nationality = models.TextField(max_length=60)
    age = models.IntegerField()
    password = models.TextField(max_length=100)
    repassword = models.TextField(max_length=100)
    
    class meta:
        db_table = 'registration'


