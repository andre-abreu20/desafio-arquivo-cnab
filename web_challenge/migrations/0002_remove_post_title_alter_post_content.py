# Generated by Django 4.1.2 on 2022-10-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_challenge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.FileField(upload_to=''),
        ),
    ]