# Generated by Django 4.1.7 on 2023-03-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0014_alter_room_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]