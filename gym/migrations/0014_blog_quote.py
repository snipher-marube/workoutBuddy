# Generated by Django 4.1.1 on 2022-09-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0013_alter_comment_blog_alter_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.TextField(blank=True, null=True),
        ),
    ]
