from django.db import models

from django.db import models

class LoginEntry(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username} ({self.phone})"

class FishModel(models.Model):
    fish_name = models.CharField(max_length=100)
    fish_description = models.TextField()
    fish_type = models.CharField(max_length=20)
    fish_size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fish_image1 = models.ImageField(upload_to='fish_images/', null=True, blank=True)
    fish_image2 = models.ImageField(upload_to='fish_images/', null=True, blank=True)
    fish_image3 = models.ImageField(upload_to='fish_images/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fish_name
