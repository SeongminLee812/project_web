# Generated by Django 3.2.5 on 2022-07-05 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoocAllList',
            fields=[
                ('num', models.AutoField(db_column='NUM', primary_key=True, serialize=False)),
                ('enrollment_start', models.DateTimeField(blank=True, null=True)),
                ('enrollment_end', models.DateTimeField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('start_display', models.CharField(blank=True, max_length=20, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('week', models.IntegerField(blank=True, null=True)),
                ('hidden', models.IntegerField(blank=True, null=True)),
                ('invitation_only', models.IntegerField(blank=True, null=True)),
                ('audit_yn', models.CharField(blank=True, max_length=3, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
                ('teachers', models.CharField(blank=True, max_length=300, null=True)),
                ('language_name', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_classfy', models.CharField(blank=True, max_length=20, null=True)),
                ('middle_classfy_name', models.CharField(blank=True, max_length=20, null=True)),
                ('fourth_industry_yn', models.CharField(blank=True, max_length=3, null=True)),
                ('ai_sec_yn', models.CharField(blank=True, max_length=3, null=True)),
                ('effort_time', models.CharField(blank=True, max_length=50, null=True)),
                ('video_time', models.CharField(blank=True, max_length=50, null=True)),
                ('learning_time', models.CharField(blank=True, max_length=50, null=True)),
                ('id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('course_id', models.CharField(blank=True, max_length=100, null=True)),
                ('star', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mooc_all_list',
                'managed': False,
            },
        ),
    ]
