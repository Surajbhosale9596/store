# Generated by Django 4.0.2 on 2022-03-17 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
