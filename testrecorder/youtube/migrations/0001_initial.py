# Generated by Django 4.0.4 on 2023-08-27 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=24, unique=True)),
                ('channel_title', models.CharField(max_length=50, unique=True)),
                ('channel_credentials', models.TextField(default='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'channels_records',
            },
        ),
        migrations.CreateModel(
            name='PlaylistsRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_id', models.CharField(max_length=250, unique=True)),
                ('playlist_title', models.CharField(max_length=250, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'playlists_records',
            },
        ),
        migrations.CreateModel(
            name='UserYoutubePlaylists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=1024)),
                ('playlist_id', models.CharField(max_length=1024)),
                ('playlist_title', models.CharField(max_length=1024)),
                ('playlist_enabled', models.BooleanField()),
            ],
            options={
                'db_table': 'user_youtube_playlists',
            },
        ),
        migrations.CreateModel(
            name='YoutubeUserCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credential', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
