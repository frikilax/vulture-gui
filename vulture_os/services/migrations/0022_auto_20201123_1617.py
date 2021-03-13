# Generated by Django 2.1.3 on 2020-11-23 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_auto_20201102_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend',
            name='cybereason_host',
            field=models.TextField(default='domain.cybereason.net', help_text='Cybereason host', verbose_name='Cybereason api endpoint'),
        ),
        migrations.AddField(
            model_name='frontend',
            name='cybereason_malops_timestamp',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='frontend',
            name='cybereason_malware_timestamp',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='frontend',
            name='cybereason_password',
            field=models.TextField(default='', help_text='Cybereason password', verbose_name='Cybereason password for authentication'),
        ),
        migrations.AddField(
            model_name='frontend',
            name='cybereason_username',
            field=models.TextField(default='', help_text='Cybereason username', verbose_name='Cybereason username for authentication'),
        ),
    ]