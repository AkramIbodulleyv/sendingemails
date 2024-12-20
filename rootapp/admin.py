from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserNotification


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')