# Generated by Django 3.0.5 on 2020-08-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_auto_20200810_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='path',
            field=models.CharField(max_length=300, null=True),
        ),
    ]