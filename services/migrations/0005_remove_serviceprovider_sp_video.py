# Generated by Django 4.0.5 on 2023-04-04 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_serviceprovider_sp_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='sp_video',
        ),
    ]