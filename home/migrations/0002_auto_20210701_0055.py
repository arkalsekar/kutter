# Generated by Django 3.1.1 on 2021-06-30 19:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Urls',
            new_name='Url',
        ),
    ]
