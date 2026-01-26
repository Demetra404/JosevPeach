from django.contrib import admin
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username','phone_number', 'country')
    list_filter = ('username',)
    search_fields = ('email', 'username')