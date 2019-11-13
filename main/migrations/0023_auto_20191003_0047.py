# Generated by Django 2.2.5 on 2019-10-02 14:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_course_slug_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='slug_url',
        ),
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
