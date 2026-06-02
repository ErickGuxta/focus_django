from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("nome",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Campos personalizados", {"fields": ("nome", "email")}),
    )
