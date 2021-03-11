# Generated by Django 2.1.3 on 2019-04-01 07:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DarwinFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField()),
                ('conf_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DarwinPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='Default policy', unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FilterPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('nb_thread', models.PositiveIntegerField(default=5)),
                ('log_level', models.TextField(choices=[('ERROR', 'Error'), ('INFO', 'Informational'), ('DEBUG', 'Debug')], default='ERROR')),
                ('status', djongo.models.fields.JSONField(default={})),
                ('threshold', models.PositiveIntegerField(default=80, help_text='Score from which the request will be blocked.', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Block threshold')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darwin.DarwinFilter')),
                ('policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darwin.DarwinPolicy')),
            ],
        ),
        migrations.CreateModel(
            name='LogViewerConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_logs', models.TextField()),
                ('displayed_columns', djongo.models.fields.JSONField()),
                ('nb_lines', models.IntegerField(default=25)),
                ('font_size', models.IntegerField(default=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.User')),
            ],
        ),
        migrations.CreateModel(
            name='LogViewerSearches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_logs', models.TextField()),
                ('name', models.TextField()),
                ('search', djongo.models.fields.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.User')),
            ],
        ),
        migrations.AddField(
            model_name='darwinpolicy',
            name='filters',
            field=models.ManyToManyField(through='darwin.FilterPolicy', to='darwin.DarwinFilter'),
        ),
        migrations.AlterUniqueTogether(
            name='logviewerconfiguration',
            unique_together={('user', 'type_logs')},
        ),
    ]
