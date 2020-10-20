from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import SignUpForm, MyUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm 
    form = MyUserChangeForm
    model = User
    list_display = ('email','username','is_staff','is_active')
    list_filter = ('is_staff','is_active')

    # fieldsets to display for updating users in admin
    fieldsets = (
        (None, {'fields': ('email','username','password')}),
        ('permissions', {'fields': ('is_staff','is_active')}),
    )

    # fieldsets to display for adding users in admin
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_active')
            }
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,CustomUserAdmin)
admin.site.unregister(Group)


