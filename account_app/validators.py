from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class TelegramUsernameValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = _('Username must start with a letter and contain only letters, numbers, and underscores.')


def max_upload_image_profile(value):
    max_size = 2 * 1024 * 1024
    image_size = value.size

    if image_size > max_size:
        raise ValidationError(
            {
                "message": _(f"Image size must be less than %(max_size)s."),
            }
        )
    return value
