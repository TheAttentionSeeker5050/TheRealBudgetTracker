"""User admin classes"""
# django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# models
from users.models import Profile
from django.contrib.auth.models import User

# # Register your models here.
# admin.site.register(Profile)

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    
    # this is how is going to be the user info showed on the user list
    list_display = ("pk","user", "phone_number", "website", "picture")
    list_display_links = ("pk", "user")
    list_editable = ("phone_number", "website", "picture")

    # to be able to search on db
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
        "phone_number"
    )

    # add filter buttons
    list_filter = (
        "created",
        "modified", 
        "user__is_active",
        "user__is_staff"
    )

    # when you click on an user, what can you edit
    fieldsets = (
        ("Profile", {
            "fields": ("user", "picture")
        }),
        ("Extra info", {
            "fields": (
                ("website", "phone_number"),
                ("biography")
            )
        }),
        ("Metadata", {
            "fields": (
                ("created", "modified"),
            ),
        })
    )

    # read only fields on the user edit page
    readonly_fields = ("created", "modified")

class ProfileInline(admin.StackedInline):
    """profile inline admin for users"""

    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff"
    )

# add the profile data edit on the user page
admin.site.unregister(User)
admin.site.register(User, UserAdmin)