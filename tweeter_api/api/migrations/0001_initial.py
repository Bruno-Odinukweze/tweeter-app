# Generated by Django 3.2.11 on 2022-01-12 10:09

from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handle',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('interval', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('message', models.CharField(max_length=100)),
                ('data', jsonfield.fields.JSONField(default=dict)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date created')),
            ],
        ),
    ]
