from django.db import models
from django.utils import timezone

from django.utils.translation import gettext_lazy as _


class CreateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class UpdateMixin(models.Model):
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    is_deleted = models.BooleanField(blank=True, null=True, editable=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True


class CoreNotification(CreateMixin, UpdateMixin, SoftDeleteMixin):
    title = models.CharField(
        max_length=255,
    )
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'core_notification'
