# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
	if request.session.get('activities') is None:
		request.session['activities'] = []
	if request.session.get('total') is None:
		request.session['total'] = 0
	return render(request,'ninjaGame/index.html')

def processMoney(request):
	if request.method == 'POST':
		if request.POST['action'] == 'farm':
			gold = random.randrange(10,21)
			task(request, gold, 'farm')
		elif request.POST['action'] == 'cave':
			gold = random.randrange(5,11)
			task(request, gold, 'cave')
		elif request.POST['action'] == 'house':
			gold = random.randrange(2,6)
			task(request, gold, 'house')
		elif request.POST['action'] == 'casino':
			gold = random.randrange(0,51)
			task(request, gold, 'casino')
	return redirect('/')

def task(request, gold, place):
	now = datetime.now()
	dateTime = now.strftime("%Y/%m/%d %I:%M %p")
	color = 'green'
	if place!= 'casino':
		stri =  "Earned {} golds from the {}! ({})".format(gold, place, dateTime)
		request.session['total'] += gold
	else:
		no = random.randrange(0,1)
		if no==0:
			stri = "Entered a casino and lost {} golds... Ouch.. ({})".format(gold, dateTime)
			color = 'red'
			request.session['total'] -= gold
		else:
			stri = "Entered a casino and won {} golds... Yayy!.. ({})".format(gold, dateTime)
			request.session['total'] += gold
	context = {
			'data': stri , 
			'color': color
			}
	request.session['activities'].append(context)

