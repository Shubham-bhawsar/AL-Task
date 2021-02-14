from django.db import models

from uuid import uuid4

# Create your models here.
class Formdata(models.Model):
    passw=models.CharField(max_length=244)
    email=models.EmailField()

class Person( models.Model):
    
    guid = models.CharField(primary_key=True, max_length=255)

    first_name = models.CharField(max_length=127,null=True, blank=True, default=None)
    last_name = models.CharField(max_length=127,null=True, blank=True, default=None)
    email = models.CharField(max_length=127, null=True, blank=True, default=None)
    phone = models.CharField(max_length=127, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name} // {self.email} ({self.guid})'
    