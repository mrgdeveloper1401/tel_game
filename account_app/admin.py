from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Profile, UserNotification


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_editable = (
        "is_active",
        "is_superuser",
        "is_staff",
    )
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("telegram_id", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "telegram_id",
        "is_staff",
        "is_active",
        "is_superuser",
        "created_at"
    )
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("username", "telegram_id")
    search_help_text = _("for search you can use username or telegram_id")
    ordering = ("telegram_id",)
    filter_horizontal = (
        "groups",
        "user_permissions"
    )
    list_per_page = 20

    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.defer(
            "is_deleted",
            "deleted_at"
        )
        return query


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    list_display = ('user', "last_name", "first_name", "created_at")
    list_per_page = 20
    search_fields = ("user__username",)
    search_help_text = _("for search you can use field username")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.only(
            "user__username",
            "first_name",
            "last_name",
            "created_at"
        )
        return queryset

admin.site.register(UserNotification)
