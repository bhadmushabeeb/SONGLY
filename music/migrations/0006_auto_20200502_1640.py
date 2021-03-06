# Generated by Django 3.0.5 on 2020-05-02 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_album_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='album_genre',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist_name',
        ),
        migrations.RemoveField(
            model_name='song',
            name='file_type',
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=250),
        ),
    ]
