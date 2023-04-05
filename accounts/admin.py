from django.contrib import admin
from .models import Account, User, UserAdmin

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_id', 'first_name',
                    'last_name', 'date_of_birth', 'email', 'phone', 'account')


admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
