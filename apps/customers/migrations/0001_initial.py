# Generated by Django 3.0.5 on 2020-04-23 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metas', '0001_initial'),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('blog', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog')),
                ('meta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metas.Meta')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
