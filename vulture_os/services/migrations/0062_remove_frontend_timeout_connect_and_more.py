# Generated by Django 4.2.6 on 2023-11-15 10:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0061_frontend_vectra_client_id_frontend_vectra_host_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontend',
            name='timeout_connect',
        ),
        migrations.AddField(
            model_name='frontend',
            name='last_update_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text="Datetime of the last frontend's update"),
        ),
    ]