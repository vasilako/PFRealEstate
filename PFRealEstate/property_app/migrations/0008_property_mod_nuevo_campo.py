# Generated by Django 4.1.3 on 2022-12-15 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0007_property_mod_user_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='property_mod',
            name='nuevo_campo',
            field=models.CharField(default=1, max_length=7),
            preserve_default=False,
        ),
    ]
