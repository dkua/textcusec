from django.contrib import admin

from .models import Group, Contact, Sender, Message


def send_message(modeladmin, request, queryset):
    for message in queryset:
        result = message.send()
        print result
send_message.short_description = "Send selected messages"

class MessageAdmin(admin.ModelAdmin):
    actions = [send_message,]


# Register models here.
admin.site.register(Group)
admin.site.register(Contact)
admin.site.register(Sender)
admin.site.register(Message, MessageAdmin)
