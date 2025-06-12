from django.db import models

from django.db import models

class LoginEntry(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username} ({self.phone})"

      