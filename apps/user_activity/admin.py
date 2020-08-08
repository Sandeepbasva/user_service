from django.contrib import admin
from .models import User, ActivityPeriod

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["user_id", "start_time", "end_time"]


admin.site.register(User, UserAdmin)
admin.site.register(ActivityPeriod, ActivityAdmin)
