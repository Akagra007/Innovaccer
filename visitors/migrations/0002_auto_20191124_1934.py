# Generated by Django 2.1.5 on 2019-11-24 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='checkout',
            field=models.TimeField(null=True),
        ),
    ]