# Generated by Django 3.1.6 on 2021-02-12 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210212_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='e_mail',
        ),
    ]
