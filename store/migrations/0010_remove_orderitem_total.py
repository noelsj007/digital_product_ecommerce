# Generated by Django 4.0.5 on 2023-02-26 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_orderitem_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total',
        ),
    ]
