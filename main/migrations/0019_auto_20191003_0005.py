# Generated by Django 2.2.5 on 2019-10-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20191003_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursevideo',
            name='link',
            field=models.TextField(max_length=11),
        ),
    ]
