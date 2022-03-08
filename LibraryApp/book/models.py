from django.db import models
from LibraryApp.authentication.models import User
class Book(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 100, default='anonymous')
    email = models.EmailField(blank = True)
    describe = models.TextField(default ='Favorite Read')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name