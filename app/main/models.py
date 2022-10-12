from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class TempGenPassword(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    password = models.CharField(max_length=30)

    def delete_record(user):
        try:
            instance = TempGenPassword.objects.get(user=user)
            instance.delete()
        except:
            return None
        
    def add_record(user, password):
        passwd = TempGenPassword()
        passwd.user = user
        passwd.password = password
        passwd.save()