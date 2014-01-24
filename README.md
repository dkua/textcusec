# TextCUSEC

A little Django project that I hacked together during [CUSEC 2014](http://2014.cusec.net "CUSEC 2014"). Originally created as a simple Python script that I used to text my UofT delegates. It got a bit unwieldy trying to keep the numbers organized so I turned the script into this Django project which makes it easy to organize and text my contacts.

If you want to play with this project you will need to clone it and install all the dependencies with pip.

```
pip install -r requirements.txt
```

You will also need to have PostgreSQL, please edit in your own database configurations in the settings module. When you first run the server, the app might complain of a missing "assets" folder. Just create a directory named assets inside the textcusec directory.

In order to get Twilio working you will need to have a "twilio.py" file in the settings module which contains the following

```
TWILIO_SID = "YOUR TWILIO ACCOUNT SID HERE"
TWILIO_TOKEN = "YOUR TWILIO AUTH TOKEN HERE"
```

This allows the app to access the Twilio API, the twilio.py file is ignored by git so should never be accidently committed.

Enjoy~
