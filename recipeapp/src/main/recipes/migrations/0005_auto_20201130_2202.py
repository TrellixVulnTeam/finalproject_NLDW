# Generated by Django 3.1.2 on 2020-11-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_recipe_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_NumServings',
            field=models.CharField(max_length=255),
        ),
    ]