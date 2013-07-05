from django.shortcuts import render

from crud.models import Person

def index(request):
	users = Person.objects.all()
	context = {'all_users': users }
	return render(request, 'index.html', context)

def adduser(request):
	pass	
	#return render(request,'adduser.html',)

def edituser(request):
	pass
	#return render(request,'edituser.html',)
	
def deleteuser(request):
	pass
	#return render(request,'deleteuser.html',)
