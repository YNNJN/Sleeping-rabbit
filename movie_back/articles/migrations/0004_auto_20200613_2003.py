# Generated by Django 3.0.7 on 2020-06-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200612_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='directorEnNm',
            new_name='directors',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='plot',
            new_name='plots',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='posterUrl',
            new_name='posters',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='directorNm',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='prodYear',
            new_name='repRlsDate',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='ratingGrade',
            new_name='stlls',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='stillUrl',
            new_name='vods',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='docid',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='releaseDate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='vodUrl',
        ),
        migrations.AlterField(
            model_name='movie',
            name='audiAcc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='movie',
            name='titleEng',
            field=models.CharField(max_length=100),
        ),
    ]
