from django.shortcuts import render, redirect
from .models import User, Travel, UserTrip, TravelManager
from django.core.urlresolvers import reverse
from django.contrib import messages
from datetime import date, datetime

def index(request):
	#Get user info with the id from session:
	user = User.objects.get(id = request.session['user'])
	context = {
	'user': User.objects.get(id = request.session['user']),
	#Get all the trips this user is going on:
	'myTrips': Travel.objects.filter(all_travel__user = user),
	#Get all the trips that user is not going on:
	'allTrips': Travel.objects.all().exclude(all_travel__user = user)
	}
	print context['allTrips']
	return render(request, 'blackBelt/index.html', context)

def plan(request):
	return render(request, 'blackBelt/plans.html')

def addTrip(request):
	if request.method == 'POST':
		flag = True
		depDate = datetime.strptime(str(request.POST['start'])[:10], '%Y-%m-%d')
		arrDate = datetime.strptime(str(request.POST['end'])[:10], '%Y-%m-%d')
		user = User.objects.get(id = request.session['user'])		
		if not Travel.objects.depDate(depDate):
			flag = False
			messages.error(request, 'Sorry, the departure date must be a date in the future')
		if not Travel.objects.arrDate(depDate, arrDate):
			flag = False
			messages.error(request, 'Sorry, the arrival date must be after the departure date')
		if flag:
			#Creating travel info
			trip = Travel.objects.create(destination=request.POST['destination'], start= request.POST['start'], end= request.POST['end'], plans= request.POST['description'], userss= user)
			user = User.objects.get(id = request.session['user'])
			# using travel info and user info to create UserTrip object:
			UserTrip.objects.create(user= user, travel=trip)
			return redirect(reverse('black:my_index'))
	return redirect(reverse('black:plans'))

def display(request, id):
	user = User.objects.filter(all_users__id = id)
	travel = Travel.objects.get(id= id)
	context = {
	#Get the trip with user associated and filter with id provided
	'myTrips': UserTrip.objects.get(id = id),
	'otherpeople': UserTrip.objects.filter(travel=travel).exclude(user=user)
	}
	return render(request, 'blackBelt/display.html', context)

def join(request, id):
	#Get id from user that is currently logged in:
	user = User.objects.get(id = request.session['user'])
	#Get travel info for the specific id:
	trip = Travel.objects.get(id=id)
	#If UserTrip already has an entry with specific id and user then..
	check = UserTrip.objects.filter(user=user).filter(travel=trip)
	if not check:
		#create UserTrip entry with provided info:
		UserTrip.objects.create(user=user, travel=trip)
	else:
		messages.error(request, "You are already going on this trip!")
	return redirect(reverse('black:my_index'))
