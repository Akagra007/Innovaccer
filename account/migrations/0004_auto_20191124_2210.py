# Generated by Django 2.1.5 on 2019-11-24 22:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_auto_20191123_2048'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userprofile',
            new_name='host',
        ),
    ]
