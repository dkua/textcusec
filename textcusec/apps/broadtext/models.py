from django.db import models
from twilio.rest import TwilioRestClient
from settings.common import TWILIO

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=15)

class Group(models.Model):
    name = models.CharField(max_length=30)
    contacts = models.ManyToManyField("Contact")

class Message(models.Model):
    sender = models.ForeignKey("Sender")
    recipients = models.ManyToManyField("Contact")
    body = models.CharField(max_length=1600)

    def send():
        result = {}
        client = sender.initiate()
        for recipient in self.recipients.all():
            number = recipient.number
            sms = client.messages.create(to=number, from_=client.number, body=self.body)
            result[number] = {"sid": sms.sid}
        return result

class Sender(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=15)

    def initiate():
        account = TWILIO.SID
        token = TWILIO.TOKEN
        return TwilioRestClient(account, token)
