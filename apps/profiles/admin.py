from django.contrib import admin
from .models.instructor import InstructorProfile
from .models.user import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Rol personalizado", {"fields": ("is_instructor",)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('is_instructor',)}),
    )


admin.site.register(InstructorProfile)
