# Generated by Django 4.0.5 on 2022-07-02 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdwithAllList',
            fields=[
                ('num', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(blank=True, max_length=1000, null=True)),
                ('lecturer', models.CharField(blank=True, max_length=100, null=True)),
                ('org', models.CharField(blank=True, max_length=100, null=True)),
                ('like_num', models.IntegerField(blank=True, null=True)),
                ('student_num', models.IntegerField(blank=True, null=True)),
                ('href', models.CharField(blank=True, max_length=1000, null=True)),
                ('level_text', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'edwith_all_list',
                'managed': False,
            },
        ),
    ]
