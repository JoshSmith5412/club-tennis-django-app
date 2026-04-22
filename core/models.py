from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    skill_level = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

# Create your models here.
