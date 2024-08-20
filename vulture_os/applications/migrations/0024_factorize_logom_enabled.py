# Generated by Django 4.2.11 on 2024-03-15 05:27

import django.core.validators
from django.db import migrations, models
import djongo.models.fields

enabled_logom = {}

def save_enabled_state(apps, schema_editor):
    logomfile_model = apps.get_model("applications", "LogOMFile")
    logomrelp_model = apps.get_model("applications", "LogOMRELP")
    logomhiredis_model = apps.get_model("applications", "LogOMHIREDIS")
    logomfwd_model = apps.get_model("applications", "LogOMFWD")
    logomelastic_model = apps.get_model("applications", "LogOMElasticSearch")
    logommongodb_model = apps.get_model("applications", "LogOMMongoDB")
    logomkafka_model = apps.get_model("applications", "LogOMKAFKA")
    db_alias = schema_editor.connection.alias
    logomfile = logomfile_model.objects.using(db_alias)
    logomrelp = logomrelp_model.objects.using(db_alias)
    logomhiredis = logomhiredis_model.objects.using(db_alias)
    logomfwd = logomfwd_model.objects.using(db_alias)
    logomelastic = logomelastic_model.objects.using(db_alias)
    logommongodb = logommongodb_model.objects.using(db_alias)
    logomkafka = logomkafka_model.objects.using(db_alias)

    for filefwd in logomfile.all():
        enabled_logom[filefwd.name] = filefwd.enabled
    for logomrelp in logomrelp.all():
        enabled_logom[logomrelp.name] = logomrelp.enabled
    for logomhiredis in logomhiredis.all():
        enabled_logom[logomhiredis.name] = logomhiredis.enabled
    for logomfwd in logomfwd.all():
        enabled_logom[logomfwd.name] = logomfwd.enabled
    for logomelastic in logomelastic.all():
        enabled_logom[logomelastic.name] = logomelastic.enabled
    for logommongodb in logommongodb.all():
        enabled_logom[logommongodb.name] = logommongodb.enabled
    for logomkafka in logomkafka.all():
        enabled_logom[logomkafka.name] = logomkafka.enabled

def restore_enabled_state(apps, schema_editor):
    logfwd_model = apps.get_model("applications", "LogOM")
    db_alias = schema_editor.connection.alias
    logfwd = logfwd_model.objects.using(db_alias)

    for fwd in logfwd.all():
        fwd.enabled = enabled_logom[fwd.name]
        fwd.save()

class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0023_logomhiredis_expire_key_logomhiredis_mode_and_more'),
    ]

    operations = [
        migrations.RunPython(save_enabled_state, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='logomelasticsearch',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logomfile',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logomfwd',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logomhiredis',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logomkafka',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logommongodb',
            name='enabled',
        ),
        migrations.RemoveField(
            model_name='logomrelp',
            name='enabled',
        ),
        migrations.AddField(
            model_name='logom',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.RunPython(restore_enabled_state, migrations.RunPython.noop),
        migrations.AddField(
            model_name='logom',
            name='spool_directory',
            field=models.TextField(null=False, default='/var/tmp', help_text='Defines an existing folder to store queue files into', validators=[django.core.validators.RegexValidator(message="Value should be a valid fullpath, beginning with a '/'", regex='^/.*$')], verbose_name='Existing folder to store queue files to'),
        ),
        migrations.AddField(
            model_name='logomelasticsearch',
            name='retry_on_els_failures',
            field=models.BooleanField(default=False, help_text="Let Rsyslog's Elasticsearch module handle and retry insertion failure", verbose_name='Handle failures and retries on ELS insertion'),
        ),
        migrations.AlterField(
            model_name='logomelasticsearch',
            name='x509_certificate',
            field=models.ForeignKey(default=None, help_text='X509Certificate object to use.', null=True, on_delete=django.db.models.deletion.CASCADE, to='system.x509certificate'),
        ),
        migrations.AlterField(
            model_name='logom',
            name='high_watermark',
            field=models.PositiveIntegerField(null=False, default=8000, help_text='Target of the high watermark', validators=[django.core.validators.MinValueValidator(100)], verbose_name='High watermark target'),
        ),
        migrations.AlterField(
            model_name='logom',
            name='low_watermark',
            field=models.PositiveIntegerField(null=False, default=6000, help_text='Set the value of the low watermark', validators=[django.core.validators.MinValueValidator(100)], verbose_name='Low watermark target'),
        ),
        migrations.AlterField(
            model_name='logom',
            name='max_disk_space',
            field=models.IntegerField(null=False, default=0, help_text='Limit the maximum disk space used by the queue in MB', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Max disk space used by the queue in MB (set to zero to disable)'),
        ),
        migrations.AlterField(
            model_name='logom',
            name='max_file_size',
            field=models.IntegerField(null=False, default=256, help_text='Set the value of the queue in MB', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Max file size of the queue in MB'),
        ),
    ]
