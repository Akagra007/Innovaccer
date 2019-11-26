from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
# Create your models here.
class visitors(models.Model):
	name= models.CharField(max_length=100)
	phone=models.CharField(max_length=10, validators=[MinLengthValidator(10),])
	email=models.EmailField(max_length=250)

	def __str__(self):
		return self.name


class meeting(models.Model):
	vid= models.ForeignKey(visitors, on_delete=models.CASCADE)
	checkin=models.CharField(max_length=2000)
	checkout=models.CharField(max_length=200,null=True)
	hid= models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.vid.name
