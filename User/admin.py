from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("id", "username", "password")}),
        (("Personal info"), {"fields": ("email",)}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": (
                "wide",), "fields": (
                "id", "username", "email", "password1", "password2"), }, ), )
    list_display = ('email', 'username')
    list_filter = ('groups', 'is_staff', 'is_superuser')
    search_fields = ('email__startswith', 'username__startswith')


# Register Models
admin.site.register(CustomUser, CustomUserAdmin)
