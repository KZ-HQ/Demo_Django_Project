# Generated by Django 2.2.5 on 2019-10-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20191002_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
