# Generated by Django 4.1.7 on 2023-03-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wydarzenia", "0005_rename_price_message_cena_remove_message_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
    ]
