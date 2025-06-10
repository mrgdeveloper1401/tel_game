from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from account_app.validators import TelegramUsernameValidator, max_upload_image_profile
from core_app.models import CreateMixin, UpdateMixin, SoftDeleteMixin


class User(AbstractBaseUser, CreateMixin, UpdateMixin, SoftDeleteMixin):
    telegram_id = models.BigIntegerField(blank=True, null=True, editable=False)
    username = models.CharField(
        blank=True,
        null=True,
        validators=[TelegramUsernameValidator()],
    )
    email = models.EmailField(
        blank=True,
    )

    def __str__(self):
        return self.telegram_id

    class Meta:
        db_table = 'auth_user'


class Profile(CreateMixin, UpdateMixin, SoftDeleteMixin):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='profile')
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profile_images/%Y/%m/%d',
        validators=[max_upload_image_profile]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'auth_profile'


class UserNotification(CreateMixin, UpdateMixin, SoftDeleteMixin):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='notification')
    title = models.CharField(
        max_length=255,
    )
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'auth_user_notification'
