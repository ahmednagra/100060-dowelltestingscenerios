# Generated by Django 4.0.4 on 2023-08-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VpsIncomingTestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=1024)),
                ('test_description', models.CharField(default='', max_length=1024)),
                ('test_name', models.CharField(default='', max_length=1024)),
                ('user_files_timestamp', models.CharField(default='', max_length=1024)),
                ('webcam_file', models.CharField(default='', max_length=1024)),
                ('screen_file', models.CharField(default='', max_length=1024)),
                ('merged_webcam_screen_file', models.CharField(default='', max_length=1024)),
                ('key_log_file', models.FileField(blank=True, upload_to='')),
                ('beanote_file', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MegaTestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=1024)),
                ('test_description', models.CharField(default='', max_length=1024)),
                ('test_name', models.CharField(default='', max_length=1024)),
                ('webcam_file', models.CharField(default='', max_length=1024)),
                ('screen_file', models.CharField(default='', max_length=1024)),
                ('merged_webcam_screen_file', models.CharField(default='', max_length=1024)),
                ('key_log_file', models.CharField(default='', max_length=1024)),
                ('beanote_file', models.CharField(default='', max_length=1024)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mega_test_records',
            },
        ),
        migrations.CreateModel(
            name='TestRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=250)),
                ('test_description', models.CharField(default='', max_length=250)),
                ('test_name', models.CharField(default='', max_length=250)),
                ('webcam_file', models.CharField(default='', max_length=250)),
                ('screen_file', models.CharField(default='', max_length=250)),
                ('merged_webcam_screen_file', models.CharField(default='', max_length=250)),
                ('key_log_file', models.FileField(blank=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'test_records_table',
            },
        ),
        migrations.CreateModel(
            name='VpsTestRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=1024)),
                ('test_description', models.CharField(default='', max_length=1024)),
                ('test_name', models.CharField(default='', max_length=1024)),
                ('user_files_timestamp', models.CharField(default='', max_length=1024)),
                ('webcam_file', models.CharField(default='', max_length=1024)),
                ('screen_file', models.CharField(default='', max_length=1024)),
                ('merged_webcam_screen_file', models.CharField(default='', max_length=1024)),
                ('key_log_file', models.CharField(default='', max_length=1024)),
                ('beanote_file', models.CharField(default='', max_length=1024)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('clickup_task_notes', models.TextField(default='')),
                ('event_id', models.CharField(default='', max_length=1024)),
                ('Account_info', models.CharField(default='', max_length=1024)),
                ('app_type', models.TextField(default='')),
            ],
            options={
                'db_table': 'vps_test_records',
            },
        ),
    ]
