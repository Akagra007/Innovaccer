from django.shortcuts import render
from django.contrib.auth.models import User, auth
from account.models import host
from django.shortcuts import redirect
from django.contrib import messages
from visitors.models import meeting, visitors
# Create your views here.
def register(request):
	if(request.method=='POST'):
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['email']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		phone=request.POST['phone']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username is not unique')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email is not unique')
				return redirect('register')
			else:	
				user= User.objects.create_user(username=username,password=password1, email=email, first_name=first_name, last_name=last_name,phone=phone)
				user.save();
				print("user created")
				return redirect('/')

		else:
			messages.info(request,'password not matching')
			return redirect('register')

	else:
		return render(request,'register.html')


'''def loginpage(request):
	# if(request.method=='POST'):
	# 	username=request.POST['username']
	# 	password=request.POST['password']
	# else:
	return render(request,'login.html')'''

def login(request):
	if request.user.is_authenticated:
		h=request.user
		meets=meeting.objects.filter(hid=h)
		context={'meets':meets}

		return render(request, 'details.html', context)
	else:
		return render(request, 'login.html')
	# if request.user.is_authenmethod=='POST':
	# 	username=request.POST['username']
	# 	password=request.POST['password']
	# 	user=auth.authenticate(username='username',password='password')

	# 	if user is not None:
	# 		auth.login(request,user)
	# 		return redirect('../details/')	
	# else:
	# 	messages.info(request,'credentials invalid')
	# 	return render(request,'login.html')
	