# Generated by Django 4.1 on 2024-05-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0004_alter_club_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="date",
            field=models.DateField(max_length=10),
        ),
    ]
