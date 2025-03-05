# Generated by Django 5.1.6 on 2025-03-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_rename_price_product_base_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variation',
            field=models.CharField(choices=[('kg', 'Kilogram'), ('L', 'Litre'), ('Dozen', 'Dozen'), ('Piece', 'Piece')], default='1kg', max_length=10),
        ),
    ]
