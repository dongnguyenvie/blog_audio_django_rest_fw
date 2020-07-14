# Generated by Django 3.0.5 on 2020-07-14 18:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('excerpt', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('ping', models.BooleanField(default=True)),
                ('status', models.CharField(default='publish', max_length=30)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('meta', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='metas.Meta')),
            ],
        ),
    ]
