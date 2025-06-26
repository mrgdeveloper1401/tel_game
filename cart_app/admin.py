from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Cart, Spring, UserSpring, UserCart, UserStep, Step


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("cart_title", "created_at", "updated_at")
    list_per_page = 20
    search_fields = ("cart_title",)
    search_help_text = _("for search you can use field cart_title")

    def get_queryset(self, request):
        return super().get_queryset(request).defer(
            "is_deleted",
            "deleted_at",
        )


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "user",
        "cart"
    )
    list_display = ('user', "cart", "created_at", 'score')
    list_per_page = 20
    search_fields = ("user__username", "cart__cart_title")
    search_help_text = _("for search you can use field username and cart_title")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            "user",
            "cart"
        ).only(
            "user__username",
            "cart_id",
            "score",
            "created_at",
        )


@admin.register(Spring)
class SpringAdmin(admin.ModelAdmin):
    list_display = ("title", "luck_number", "created_at", "updated_at", "is_active")
    list_per_page = 20
    search_fields = ("title",)
    search_help_text = _("for search you can use field title")
    list_filter = ('is_active',)
    list_editable = ("is_active",)

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "title",
            "luck_number",
            "created_at",
            "updated_at",
            "is_active"
        )


@admin.register(UserSpring)
class UserSpringAdmin(admin.ModelAdmin):
    list_display = ("user", "spring", "created_at", "created_date", "is_active")
    raw_id_fields = ("user", "spring")
    list_per_page = 20
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_help_text = _("for search you can use field username")
    search_fields = ("user__username",)

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "user__username",
            "spring__is_active",
            "created_at",
            "created_date",
            "is_active"
        )


@admin.register(UserStep)
class ModelNameAdmin(admin.ModelAdmin):
    raw_id_fields = (
        "user",
        "step"
    )
    list_display = ("user", "step", "is_active", "created_at", "updated_at")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    list_per_page = 20

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "user__username",
            "step__point",
            "is_active",
            "created_at",
            "updated_at"
        )


@admin.register(Step)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('point', "created_at", "is_active")
    list_filter = ("created_at", "is_active")
    list_per_page = 20
    list_editable = ("is_active",)

    def get_queryset(self, request):
        return super().get_queryset(request).only(
            "point",
            "created_at",
            "step_image",
            "is_active",
        )
