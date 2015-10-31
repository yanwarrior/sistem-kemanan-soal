# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('kelas', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('mata_pelajaran', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Soal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('file_soal', models.FileField(upload_to='soal/%Y/%M/')),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('guru', models.ForeignKey(to='soal.Guru')),
            ],
            options={
                'verbose_name_plural': 'App Soal',
            },
        ),
        migrations.AddField(
            model_name='guru',
            name='mata_pelajaran',
            field=models.ForeignKey(to='soal.MataPelajaran'),
        ),
        migrations.AddField(
            model_name='guru',
            name='mengajar',
            field=models.ManyToManyField(to='soal.Kelas'),
        ),
        migrations.AddField(
            model_name='guru',
            name='username',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
