# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('que', models.TextField(unique=True)),
                ('subject', models.TextField()),
                ('difficulty', models.TextField()),
                ('ref', models.ForeignKey(to='queapp.Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
