# Generated by Django 3.1.2 on 2021-01-25 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0012_recipe_discount_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
