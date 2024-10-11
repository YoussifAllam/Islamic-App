from django.db import models
from uuid import uuid4
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class supplication(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    supplication_content = CKEditor5Field('Text', config_name='extends')

    benefit = models.TextField(
        verbose_name="benefit",
        help_text="benefit",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "supplications"
        verbose_name_plural = "supplications"

    def __str__(self):
        return f'{self.supplication_content}'
