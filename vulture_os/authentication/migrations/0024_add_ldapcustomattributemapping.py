# Generated by Django 4.2.6 on 2023-11-29 15:01

import bson.objectid
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_remove_repoattributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='LDAPCustomAttributeMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ldap_attribute', models.TextField(verbose_name='LDAP internal attribute to get the value from')),
                ('output_attribute', models.TextField(verbose_name='Output field to put the value in')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.ldaprepository', verbose_name='Reference on the LDAP repository using this mapping')),
            ],
        ),
    ]
