from django.db import models

# Create your models here.
class profile_info(models.Model):
    full_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    college_name=models.CharField(max_length=50)
    office_name=models.CharField(max_length=50)
    phone_number=models.IntegerField()
