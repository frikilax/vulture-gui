# Generated by Django 3.0.5 on 2021-04-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0031_frontend_kafka_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend',
            name='netskope_apikey',
            field=models.TextField(default='', help_text='Netskope API token', verbose_name='Netskope API token used to retrieve events'),
        ),
        migrations.AddField(
            model_name='frontend',
            name='netskope_host',
            field=models.TextField(default='example.goskope.com', help_text='Hostname (without scheme or path) of the Netskope server', verbose_name='Netskope Host'),
        ),
    ]
