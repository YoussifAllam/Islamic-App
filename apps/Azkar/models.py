from django.db import models
from uuid import uuid4
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Azkar_categories(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Category Name",
        help_text="Category Name",
    )

    icon = models.ImageField(
        upload_to="azkar/category_icons/",
        verbose_name="Category Icon",
        help_text="Category Icon",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Zikr(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    zikr_category = models.ForeignKey(
        "Azkar_categories",
        on_delete=models.CASCADE,
        related_name="Azkar_set",
        verbose_name="Zikr Category",
        help_text="Zikr Category",
    )

    zikr_content = CKEditor5Field('Text', config_name='extends')

    zikr_repetitions = models.IntegerField(
        verbose_name="Zikr repetitions",
        help_text="Zikr repetitions",
    )

    binifit = models.TextField(
        verbose_name="Binifit",
        help_text="Binifit",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "zikr"
        verbose_name_plural = "Azkar"

    def __str__(self):
        return f'{self.zikr_category.name}, {self.zikr_content}'
