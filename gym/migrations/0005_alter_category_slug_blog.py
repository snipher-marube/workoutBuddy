# Generated by Django 4.1.1 on 2022-09-17 12:43

import autoslug.fields
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_alter_category_category_name_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='category_name', unique=True),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('intro', models.TextField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, to='gym.category')),
                ('tag', models.ManyToManyField(blank=True, null=True, to='gym.tag')),
            ],
        ),
    ]
