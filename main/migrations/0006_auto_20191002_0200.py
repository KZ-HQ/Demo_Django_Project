# Generated by Django 2.2.5 on 2019-10-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191001_0328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='source',
            new_name='source_link',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.CharField(default='Unspecified', max_length=100),
        ),
    ]
