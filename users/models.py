from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	#image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	full_name = models.CharField(blank=True, max_length=50)
	points = models.CharField(blank=True, max_length=50, default="0")

	def __str__(self):
		return f'{self.user.username} Profile' 


	def save(self, ** kwargs):
		super().save()
