# Generated by Django 3.0.5 on 2020-08-10 10:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('excerpt', models.TextField(blank=True, default='')),
                ('content', models.TextField(blank=True, default='')),
                ('resource', models.TextField(blank=True, null=True)),
                ('ping', models.BooleanField(default=True)),
                ('type', models.IntegerField(choices=[(1, 'post'), (2, 'video'), (3, 'audio'), (4, 'image'), (5, 'other')], default=1)),
                ('status', models.CharField(default='publish', max_length=30)),
                ('isDeleted', models.BooleanField(default=False)),
                ('thumbnail', models.URLField(blank=True, default='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
