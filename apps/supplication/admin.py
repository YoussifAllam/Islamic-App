from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import supplication


@admin.register(supplication)
class supplicationAdminClass(ModelAdmin):
    list_display = (
        "uuid",
        "supplication_content",
    )
