from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCrationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCrationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets+(
        (None, {
            "fields": (
                'age',
            ),
        }),
    )
    add_fieldsets = UserAdmin.fieldsets+(
        (None, {
            "fields": (
                'age',
            ),
        }),
    )


admin.site.register(CustomUser,CustomUserAdmin)