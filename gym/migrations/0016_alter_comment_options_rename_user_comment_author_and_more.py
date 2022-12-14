# Generated by Django 4.1.1 on 2022-09-19 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0015_alter_blog_quote'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date_added',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='timestamp',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='comm_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=400),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.profile')),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='gym.comment')),
            ],
        ),
    ]
