# Generated by Django 3.1.2 on 2020-11-24 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20201124_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_total',
        ),
    ]
