# Generated by Django 3.0.5 on 2020-08-10 10:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('parrentId', models.UUIDField(blank=True, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('user', models.TextField(blank=True, default='', null=True)),
                ('view', models.BigIntegerField(default=0)),
                ('like', models.BigIntegerField(default=0)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]