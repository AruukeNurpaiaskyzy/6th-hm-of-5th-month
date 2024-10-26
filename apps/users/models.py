from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.phone
    
    class Meta:
        verbose_name_plural = 'данные'