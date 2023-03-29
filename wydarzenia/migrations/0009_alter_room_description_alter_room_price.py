# Generated by Django 4.1.7 on 2023-03-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0008_merge_20230321_1227"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
