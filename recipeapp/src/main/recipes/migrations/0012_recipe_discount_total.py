# Generated by Django 3.1.2 on 2021-01-18 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20201215_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='discount_total',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=20),
        ),
    ]
