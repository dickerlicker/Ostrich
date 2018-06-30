# Generated by Django 2.0.6 on 2018-06-28 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ranges', '0002_auto_20180626_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnavailablePorts',
            fields=[
                ('portnumber', models.IntegerField(db_column='portnNumber', primary_key=True, serialize=False)),
                ('studentid', models.ForeignKey(db_column='studentid', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UnavailablePorts',
                'verbose_name_plural': 'UnavailablePorts',
            },
        ),
    ]
