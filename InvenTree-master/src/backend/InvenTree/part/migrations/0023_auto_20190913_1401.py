# Generated by Django 2.2.5 on 2019-09-13 14:01

import InvenTree.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0022_auto_20190908_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='URL',
            field=InvenTree.fields.InvenTreeURLField(blank=True, help_text='Link to external URL'),
        ),
    ]
