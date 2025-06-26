from django.core import exceptions
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from account_app.validators import TelegramUsernameValidator, max_upload_image_profile
from core_app.models import CreateMixin, UpdateMixin, SoftDeleteMixin


class User(AbstractBaseUser, CreateMixin, UpdateMixin, SoftDeleteMixin, PermissionsMixin):
    telegram_id = models.BigIntegerField(
        unique=True,
    )
    username = models.CharField(
        blank=True,
        null=True,
        unique=True,
        validators=[TelegramUsernameValidator()],
    )
    email = models.EmailField(
        blank=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, obj):
        return True

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
        validators=(max_upload_image_profile,),
        blank=True,
        null=True
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


class UserInvite(CreateMixin, UpdateMixin, SoftDeleteMixin):
    from_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='from_user_invite',
                                  help_text=_("از کاربر"))
    to_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='to_user_invite',
                                help_text=_("به کاربر"))
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "user_invite"
        unique_together = (
            "from_user",
            "to_user"
        )

    # validate not same from_user and to_user
    def clean(self):
        if self.pk is None:
            if self.from_user.id == self.to_user.id:
                raise exceptions.ValidationError(
                    {
                        "from_user": _("from_user and to_user not be the same"),
                    }
                )
