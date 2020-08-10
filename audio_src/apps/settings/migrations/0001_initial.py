# Generated by Django 3.0.5 on 2020-08-10 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=30)),
                ('value', models.TextField()),
                ('option', models.TextField()),
                ('isDeleted', models.BooleanField(default=False)),
                ('default', models.TextField(default='')),
            ],
        ),
    ]
