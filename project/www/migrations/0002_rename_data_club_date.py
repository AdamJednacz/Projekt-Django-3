# Generated by Django 4.1 on 2024-05-20 16:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="club",
            old_name="data",
            new_name="date",
        ),
    ]
