from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Beer(models.Model):
	name = models.CharField(max_length=100)
	attr1 = models.CharField(max_length=50, default='00000')
	val1 = models.IntegerField(default=0)
	attr2 = models.CharField(max_length=50, default='00000')
	val2 = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name

	def foo(self):
		return self.attr1

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	favBeer = models.ForeignKey(Beer)
	uName = models.CharField(max_length=50)

	def __str__(self):
		return self.uName

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])