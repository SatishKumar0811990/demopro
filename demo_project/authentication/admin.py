from django.contrib import admin

# Register your models here.
from .models import User,Links


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',  'created_at']


admin.site.register(User, UserAdmin)



@admin.register(Links)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['url_type','link']

