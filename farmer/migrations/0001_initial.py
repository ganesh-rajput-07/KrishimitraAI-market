# Generated by Django 5.1.6 on 2025-03-01 05:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='farmer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='farmer.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='products/')),
                ('category', models.CharField(choices=[('vegetables', 'Vegetables'), ('fruits', 'Fruits'), ('dairy', 'Dairy'), ('grains', 'Grains'), ('other', 'Other')], max_length=20)),
                ('quantity_variation', models.CharField(choices=[('1kg', '1 kilogram'), ('2kg', '2 kilograms'), ('1l', '1 liter'), ('2l', '2 liters'), ('1dz', '1 Dozen'), ('2dz', '2 Dozen')], default='1kg', max_length=10)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='farmer.farmer')),
            ],
        ),
    ]
