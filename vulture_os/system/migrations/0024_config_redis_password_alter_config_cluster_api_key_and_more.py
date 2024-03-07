# Generated by Django 4.2.7 on 2024-02-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0023_alter_messagequeue_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='redis_password',
            field=models.TextField(blank=True, default='', help_text='Set the password for local Redis cluster', null=True, verbose_name='Redis cluster password'),
        ),
        migrations.AlterField(
            model_name='config',
            name='cluster_api_key',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='config',
            name='portal_cookie_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='config',
            name='public_token',
            field=models.TextField(default=''),
        ),
    ]