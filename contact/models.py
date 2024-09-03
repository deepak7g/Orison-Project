from django.db import models

# Create your models here.


class storeDB(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    messaged_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    