# Generated by Django 4.2.19 on 2025-02-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('fuel_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
