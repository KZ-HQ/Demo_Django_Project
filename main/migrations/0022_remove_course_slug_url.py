# Generated by Django 2.2.5 on 2019-10-02 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_coursevideo_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slug_url',
        ),
    ]
