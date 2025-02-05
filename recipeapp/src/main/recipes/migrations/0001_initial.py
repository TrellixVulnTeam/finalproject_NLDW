# Generated by Django 3.1.2 on 2020-11-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productitem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=255)),
                ('equivalent_product', models.ManyToManyField(blank=True, to='productitem.Item')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=255, unique=True)),
                ('recipe_total', models.DecimalField(decimal_places=10, max_digits=20)),
                ('recipe_link', models.CharField(max_length=255)),
                ('recipe_rating', models.CharField(max_length=255)),
                ('recipe_numRatings', models.IntegerField()),
                ('recipe_image', models.CharField(max_length=255)),
                ('recipe_NumServings', models.CharField(blank=True, max_length=255)),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
                ('recipe_category', models.ManyToManyField(to='recipes.RecipeCategory')),
            ],
        ),
    ]
