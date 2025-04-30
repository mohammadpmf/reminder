from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    model = Reminder
    list_display = ["user", "title", "period", "active"]
    list_display_links = ["user", "title", "period", "active"]
