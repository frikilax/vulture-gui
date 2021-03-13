# Generated by Django 2.1.3 on 2021-02-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0013_auto_20201005_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='pf_custom_nat_config',
            field=models.TextField(blank=True, default='### Custom NAT rules\n'),
        ),
        migrations.AddField(
            model_name='node',
            name='pf_custom_param_config',
            field=models.TextField(blank=True, default='### Custom global parameters\n'),
        ),
        migrations.AddField(
            model_name='node',
            name='pf_custom_rdr_config',
            field=models.TextField(blank=True, default='### Custom RDR rules\n'),
        ),
    ]