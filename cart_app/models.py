from django.db import models
from django.utils.translation import gettext_lazy as _

from core_app.models import CreateMixin, UpdateMixin, SoftDeleteMixin


class Cart(CreateMixin, UpdateMixin, SoftDeleteMixin, models.Model):
    cart_title = models.CharField(
        max_length=255,
        verbose_name=_("عنوان کارت")
    )
    cart_image = models.ImageField(
        upload_to="cart_images/%Y/%m/%d",
    )
    description = models.TextField()

    class Meta:
        db_table = "cart"


class UserCart(CreateMixin, UpdateMixin, SoftDeleteMixin):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name="cart_user_cart"
    )
    user = models.ForeignKey(
        "account_app.User",
        on_delete=models.PROTECT,
        related_name="user_user_cart"
    )
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "user_cart"


class Spring(CreateMixin, UpdateMixin, SoftDeleteMixin):
    title = models.CharField(
        max_length=255,
        verbose_name=_("نام یا عنوان")
    )
    spring_image = models.ImageField(
        upload_to="spring_images/%Y/%m/%d"
    )
    luck_number = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "spring"


class UserSpring(CreateMixin, UpdateMixin, SoftDeleteMixin):
    user = models.ForeignKey(
        "account_app.User",
        related_name="user_user_spring",
        on_delete=models.PROTECT
    )
    spring = models.ForeignKey(
        Spring,
        related_name="spring_user_spring",
        on_delete=models.PROTECT,
    )
    created_date = models.DateField(
        auto_now_add=True,
        editable=False
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_spring"

        # یکتا سازی روی (user, created_date)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'created_date'],
                name='unique_active_user_per_day',
                condition=models.Q(is_active=True),
            )
        ]
