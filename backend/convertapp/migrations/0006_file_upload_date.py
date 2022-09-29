# Generated by Django 4.1.1 on 2022-09-29 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("convertapp", "0005_file_extension_alter_file_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="upload_date",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]