# Generated by Django 4.1.1 on 2022-09-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("convertapp", "0004_file_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="file",
            name="extension",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="uploads"),
        ),
    ]
