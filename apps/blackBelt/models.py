from __future__ import unicode_literals
from django.db import models
from ..loginReg.models import User
from datetime import date, datetime

class TravelManager(models.Manager):
	def depDate(self, date):
		today = datetime.strptime(str(date.today())[:10], '%Y-%m-%d')
		difference = (date - today).days
		if difference <= 0:
			return False
		else:
			return True
	def arrDate(self, depDate, arrDate):
		difference = (arrDate - depDate).days
		if difference <= 0:
			return False
		else:
			return True

class Travel(models.Model):
	destination = models.CharField(max_length = 255)
	start = models.DateTimeField()
	end = models.DateTimeField()
	plans = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userss = models.ForeignKey(User, related_name = 'users_on_trip')
	objects = TravelManager()

class UserTrip(models.Model):
	user = models.ForeignKey(User, related_name="all_users")
	travel = models.ForeignKey(Travel, related_name="all_travel")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	# class User(models.Model):
	# name = models.CharField(max_length = 30)
	# username = models.CharField(max_length = 30)
	# password = models.CharField(max_length=100)
	# created_at = models.DateTimeField(auto_now_add = True)
	# updated_at = models.DateTimeField(auto_now = True)
	
	# objects = UserManager()


