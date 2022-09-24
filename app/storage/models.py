from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth import get_user_model
# Create your models here.


class PasswordStorage(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    site = models.URLField(verbose_name="Site url")
    password = models.CharField(max_length=128, help_text='Write you password, max length 128 chars')
    key = models.BinaryField(blank=True, null=True,)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('storage_detail', args=[str(self.id)])
    
    def create_passwd_from_generator(self, user, site, password, key):
        new_passwd = PasswordStorage
        new_passwd.user = user
        new_passwd.site = site
        new_passwd.password = password
        new_passwd.key = key
        new_passwd.save()
    
    class Meta:
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'
        
