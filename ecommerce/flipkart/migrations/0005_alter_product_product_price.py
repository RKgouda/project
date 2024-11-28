# Generated by Django 5.0.6 on 2024-11-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flipkart", "0004_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_price",
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=10),
        ),
    ]