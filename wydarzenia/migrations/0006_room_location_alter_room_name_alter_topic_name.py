# Generated by Django 4.1.6 on 2023-03-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0005_rename_price_message_cena_remove_message_body_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="location",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="topic",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
