# Generated by Django 3.0.5 on 2020-04-17 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        ('customers', '0004_auto_20200417_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='blog',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Blog'),
        ),
    ]