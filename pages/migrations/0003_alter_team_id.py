# Generated by Django 4.1.7 on 2023-08-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0002_auto_20230731_2223"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
