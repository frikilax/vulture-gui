# Generated by Django 2.1.3 on 2020-09-15 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20200915_1600'),
        ('workflow', '0004_auto_20190904_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='authentication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.UserAuthentication'),
        ),
    ]