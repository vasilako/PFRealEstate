# Generated by Django 4.1.3 on 2022-12-14 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_agent_app', '0003_remove_useragent_mod_manage_properties_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useragent_mod',
            name='manage_properties',
        ),
    ]