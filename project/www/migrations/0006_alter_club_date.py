# Generated by Django 4.1 on 2024-05-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("www", "0005_alter_club_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="club",
            name="date",
            field=models.DateTimeField(max_length=10),
        ),
    ]