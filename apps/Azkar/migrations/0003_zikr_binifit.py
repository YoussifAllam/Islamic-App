# Generated by Django 5.0.6 on 2024-10-10 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Azkar", "0002_alter_zikr_zikr_repetitions"),
    ]

    operations = [
        migrations.AddField(
            model_name="zikr",
            name="binifit",
            field=models.TextField(
                blank=True, help_text="Binifit", null=True, verbose_name="Binifit"
            ),
        ),
    ]
