# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyconkr', '0004_auto_20150816_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['id']},
        ),
    ]
