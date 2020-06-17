from django.db import models
from django.contrib.auth.models import User #default USER class imported

# Create your models here.

class UserRegister(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    mobile_number=models.IntegerField(max_length=10)
    date_of_birth=models.DateField()
    # profile_pic=models.ImageField(upload_to=)
    def __str__(self):
        return self.user.username

