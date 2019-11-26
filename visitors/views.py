from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from visitors.models import visitors,meeting
from account.models import host
from django.contrib import messages
from django.contrib.auth.models import User
from twilio.rest import Client
from dateutil import parser as date_parser
# Create your views here.
def checkin(request):
	if request.method=='POST':
		name=request.POST['name']
		phone=request.POST['phone']
		email=request.POST['email']
		hostemail=request.POST['h-email']
		checkin=request.POST['checkin']
		if User.objects.filter(email=hostemail).exists():
			v=visitors(name=name,phone=phone,email=email)
			v.save()
			#vis=visitors.objects.get(email=email)
			h=User.objects.get(email=hostemail)
			hos=h.host
			m=meeting(vid=v, checkin=str(checkin), hid=h)
			m.save()
			subject = 'Visitor Details'
			message = "Name-"+name+"\n"+"Email-"+email+"\n"+"Phone-"+phone+"\n"+"Checkin Time-"+checkin+"\n"
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [hostemail,]    
			send_mail( subject, message, email_from, recipient_list )  
						# Download the helper library from https://www.twilio.com/docs/python/install
			


			# Your Account Sid and Auth Token from twilio.com/console
			# DANGER! This is insecure. See http://twil.io/secure
			account_sid = 'ACd5ab35d25c1c3816c56d19f077e97901'
			auth_token = 'd2a33aacfd0f0800531946e36bef127e'
			client = Client(account_sid, auth_token)

			message = client.messages \
			                .create(
			                     body='Name-'+name+'\n'+'Email-'+email+'\n'+'Phone-'+phone+'\n'+'Checkin Time-'+checkin+'\n',
			                     from_='+17326622671',
			                     to='+91'+str(hos.phone)
			                 ) 

			return redirect('../../')
		else:
			messages.info(request,'host email does not exist')
			return redirect('../checkin/')

	# User.objects.all().delete()
	# host.objects.all().delete()
	# visitors.objects.all().delete()
	# meeting.objects.all().delete()
	return render(request,'checkin.html')


def checkout(request):
	if request.method=='POST':
		checkout=request.POST['checkout']
		email=request.POST['email']
		if visitors.objects.filter(email=email).exists():
			v=visitors.objects.get(email=email)
			m=meeting.objects.filter(vid=v, checkout__isnull=True).order_by('-id')
			if len(m)==0:
				a=5
			else:
				m=m[0]
				m.checkout=checkout
				m.save()
				u=m.hid
			#u=User.objects.get(user_id=h)
			#hostobj=host.objects.get(user=u.username)
				hostobj=u.host
				subject = 'Visitors Details'
				message = 'Host Name-'+u.first_name+'\n'+'Email-'+u.email+'\n'+'Phone-'+hostobj.phone
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [email,]    
				send_mail( subject, message, email_from, recipient_list )  
				return redirect('../../')
		else:
			messages.info(request,'email does not exist')
			return redirect('../checkout/')

	return render(request,'checkout.html')

# def email(request):    
# 	subject = 'Thank you for registering to our site'
#     message = ' it  means a world to us '
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['receiver@gmail.com',]    
#     send_mail( subject, message, email_from, recipient_list )    
#     return redirect('redirect to a new page')