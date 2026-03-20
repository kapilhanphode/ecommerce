from django.contrib import admin
from apps.accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'email',)
    search_fields = ('name', 'email',)
    list_filter = ('email',)

