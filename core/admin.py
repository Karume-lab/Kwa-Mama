from django.contrib import admin
from . import models


# Register your models here.
class ContactMessage(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "message",
        "created_at",
    ]


admin.site.register(models.ContactMessage, ContactMessage)
