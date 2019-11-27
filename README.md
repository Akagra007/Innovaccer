# Innovaccer
Innovaccer assignment for internship

## Description
This is a entry management software. We have integrated it with SMS API and mail services using SMTP server.

## Tech Stack
Frontend : HTML 5, CSS, JS<br />
Backend  : Django (1.11.26) [Installation Link](https://www.djangoproject.com/)<br /> 
Security : Bcrypt (3.1.5) used in Django __pip install bcrypt__(use this command in terminal to install bcrypt)<br />
SMS API  : Twilio [Website](https://www.twilio.com/)
Language : Python3 [Installation Link](https://www.python.org/downloads/)

## Setup Installation

#### Setup SMS services
Go to [Twilio](https://www.twilio.com/). __Sign in using ID(17ucs012@lnmiit.ac.in) and Password(AKAGRAGUPTA12345)__. Now you have to register your Host Phone Numbers [here](https://www.twilio.com/console/phone-numbers/verified) or folloe this All product and Services--> Phone Numbers--> Verified Caller ID and add Host Phone Numbers.

Now your phone numbers are ready to accept messages from this software.

#### Setup Project
As you Downloaded the zip folder.First extract the files to a folder and name it "office". Open the terminal and go to the location where you can find manage.py file. Now give command python3 manage.py runserver. Now your Localhost:8000 is activated run this server on your web browsers. Here you can see the main screen.

#### Register your hosts
Click on the register button and it will redirect you to the admin login page.__(Username: akagra and Password: office)__ now you will enter the admin section and here you can see the databases. Now go to Users and open it.<br />
<img src = "https://github.com/Akagra007/Innovaccer/blob/master/images/User%20Model.jpeg" align = "rigth" width="350px"><br />
Now click on add user on top right corner<br />
<img src = "https://github.com/Akagra007/Innovaccer/blob/master/images/Add%20User.jpeg" align = "rigth" width="350px"><br />
Now fill details and click on save and continue editing and fill rest of the details.<br />
<img src = "https://github.com/Akagra007/Innovaccer/blob/master/images/saveandcontinue.jpeg" align = "rigth" width="350px"><br />

Now your Host has been added. Now the Software is ready to Work.
Now go to localhost:8000 again

## Workflow around the Software
__Checkin Button__ use to check in, fill up the form. When form is submitted SMS and a mail in recieved by the respected Host.<br />
__CheckOut Button__ use to checkout, fill up the form. When form is submitted a mail in recieved by the respected visitor.<br />
__Login Button__ admin login page to check his history of meeting.






