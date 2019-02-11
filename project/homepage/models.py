from django.db import models

class Contactus(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
