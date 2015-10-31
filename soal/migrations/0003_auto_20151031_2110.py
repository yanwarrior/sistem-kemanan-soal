# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soal', '0002_auto_20151031_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordManager',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(unique=True, max_length=8)),
                ('guru', models.OneToOneField(to='soal.Guru')),
            ],
        ),
        migrations.AlterField(
            model_name='soal',
            name='file_soal',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
