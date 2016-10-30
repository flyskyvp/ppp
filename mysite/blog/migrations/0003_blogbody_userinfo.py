# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBody',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_body', models.TextField()),
                ('blog_type', models.CharField(max_length=50)),
                ('blog_timestamp', models.DateTimeField()),
                ('blog_imgurl', models.CharField(max_length=50, null=True)),
                ('blog_author', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=20)),
                ('work', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
