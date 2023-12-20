# Generated by Django 4.2.7 on 2023-12-19 15:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_alter_tlsprofile_protocols'),
        ('applications', '0021_auto_20231006_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='tls_profile',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='system.tlsprofile'),
        ),
    ]
