from django.db import models

from apps.users.models import User

# Create your models here.
class List(models.Model):
    user = models.CharField(max_length=155)
    title = models.CharField(max_length=155)
    description = models.TextField(max_length=155)
    is_completed= models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='to_do_images/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name=""
        verbose_name_plural="тоже какие то данные "
