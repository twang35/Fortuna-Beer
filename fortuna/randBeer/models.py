from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Beer(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100)
	rating = models.IntegerField(default=2.5)
	creation_date = models.DateTimeField(auto_now=True, blank=True)
	
	def __str__(self):
		return self.name

	def foo(self):
		return self.rating

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	uName = models.CharField(max_length=50)

	def __str__(self):
		return self.uName

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])