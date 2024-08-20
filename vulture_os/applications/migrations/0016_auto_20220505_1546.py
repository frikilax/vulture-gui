# Generated by Django 3.0.5 on 2022-05-05 15:46

import django.core.validators
from django.db import migrations, models
from toolkit.mongodb.mongo_base import MongoBase


def remove_server_target_port_unicity_constraint(apps, schema_editor):
    # Manually delete all Darwin filters to prevent migration issue, they will be re-created in loaddata
    m = MongoBase()
    m.connect_primary()
    # If the node is not yet installed, no need to drop collections
    if m.db and m.db['vulture'] is not None:
        coll = m.db['vulture']['applications_server']
        if coll is not None:
            for index in coll.list_indexes():
                # Unpack index key values
                # we're searching for 'target' and 'port' keys defining the index
                if ['target', 'port'] == index.get('key', {}).keys():
                    print(f"Removing index {index.get('name')} in column 'applications_server'")
                    coll.drop_index(index.get('name'))

class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0015_logomfwd_send_as_raw'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='server',
            unique_together=None,
        ),
        migrations.RunPython(remove_server_target_port_unicity_constraint, migrations.RunPython.noop),
    ]
