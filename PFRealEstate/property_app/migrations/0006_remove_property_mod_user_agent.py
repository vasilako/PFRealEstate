# Generated by Django 4.1.3 on 2022-12-14 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0005_alter_address_mod_city_alter_address_mod_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_mod',
            name='user_agent',
        ),
    ]
