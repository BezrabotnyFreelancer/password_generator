from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth import get_user_model
# Create your models here.


class PasswordStorage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    site = models.URLField(verbose_name="Site url")
    password = models.CharField(max_length=128, help_text='Write a password between 8 and 128 characters')
    key = models.BinaryField(blank=True, null=True,)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('storage_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
        
