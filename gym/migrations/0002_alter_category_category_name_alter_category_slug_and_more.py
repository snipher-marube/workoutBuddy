# Generated by Django 4.1.1 on 2022-09-17 11:01

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(blank=True, max_length=255, null=True, unique=True)),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
