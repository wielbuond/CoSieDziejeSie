# Generated by Django 4.1.7 on 2023-03-30 07:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0018_room_time_alter_room_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="time",
        ),
        migrations.AlterField(
            model_name="room",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
