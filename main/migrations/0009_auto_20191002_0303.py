# Generated by Django 2.2.5 on 2019-10-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191002_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]