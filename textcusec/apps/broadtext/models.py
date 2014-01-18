from django.db import models
from twilio.rest import TwilioRestClient
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=15)

    def __unicode__(self):
        return u"{0}: {1}".format(self.name, self.number)

class Group(models.Model):
    name = models.CharField(max_length=30)
    contacts = models.ManyToManyField("Contact")

    def __unicode__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey("Sender")
    contacts = models.ManyToManyField("Contact", blank=True)
    groups = models.ManyToManyField("Group", blank=True)
    body = models.CharField(max_length=1600, blank=True)

    def __unicode__(self):
        return self.body[:50]

    def send(self):
        result = {}
        client = self.sender.initiate()
        recipients = self.contacts.all()
        for group in self.groups.all():
            recipients = recipients | group.contacts.all()
        for recipient in recipients.distinct():
            number = recipient.number
            sms = client.messages.create(to=number, from_=self.sender.number, body=self.body)
            result[number] = {"sid": sms.sid}
        return result

class Sender(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=15)

    def __unicode__(self):
        return u"{0}: {1}".format(self.name, self.number)

    def initiate(self):
        account = settings.TWILIO_SID
        token = settings.TWILIO_TOKEN
        return TwilioRestClient(account, token)
