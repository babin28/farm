from django.db import models

from django.db import models

class LoginEntry(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.username} ({self.phone})"

      
# class FishModel
"""DB for fish -> fish_name, fish_description, fish_type, fish_size, price, fish_image1, fish_image2, fish_image3, is_active"""
