# Generated by Django 3.0.7 on 2020-06-15 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='repRlsDate',
            field=models.CharField(max_length=10),
        ),
    ]