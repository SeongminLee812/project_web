# Generated by Django 4.0.5 on 2022-07-05 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kocw', '0002_alter_kocwalllist_options'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='kocwalllist',
            table='kocw_all_list',
        ),
    ]