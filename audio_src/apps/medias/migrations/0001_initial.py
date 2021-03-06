# Generated by Django 3.0.5 on 2020-08-10 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=350)),
                ('type', models.IntegerField(choices=[(1, 'drive'), (2, 's3'), (2, 'local')], default=1)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
