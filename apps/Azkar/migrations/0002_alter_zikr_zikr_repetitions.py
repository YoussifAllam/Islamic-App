# Generated by Django 5.0.6 on 2024-10-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Azkar", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zikr",
            name="zikr_repetitions",
            field=models.IntegerField(
                help_text="Zikr repetitions", verbose_name="Zikr repetitions"
            ),
        ),
    ]
