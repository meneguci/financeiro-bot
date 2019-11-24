# Generated by Django 2.2.6 on 2019-11-23 20:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NubankItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('post_date', models.DateField()),
                ('nubank_id', models.CharField(max_length=40)),
                ('href', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=80)),
                ('charges', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NubankItem2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount_without_iof', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=80)),
                ('item_type', models.DateTimeField(help_text='2019-11-23T19:13:43Z', verbose_name='time')),
                ('source', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=40)),
                ('details', django.contrib.postgres.fields.jsonb.JSONField()),
                ('nubank_id', models.CharField(max_length=40, verbose_name='id')),
                ('href', models.CharField(max_length=200)),
                ('index', models.IntegerField()),
                ('charges', models.IntegerField()),
            ],
        ),
    ]