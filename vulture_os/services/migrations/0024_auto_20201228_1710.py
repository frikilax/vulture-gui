# Generated by Django 2.1.3 on 2020-12-28 17:10

import django.core.validators
from django.db import migrations, models
import djongo.models.fields

class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_auto_20201201_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend',
            name='cisco_meraki_apikey',
            field=models.TextField(default='', help_text='API key used to retrieve logs - as configured in Meraki settings', verbose_name='Cisco Meraki API key'),
        ),
        migrations.AddField(
            model_name='frontend',
            name='cisco_meraki_timestamp',
            field=djongo.models.fields.DictField(default={}, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frontend',
            name='cisco_meraki_timestamp',
            field=djongo.models.fields.DictField(default={}),
        ),
    ]
