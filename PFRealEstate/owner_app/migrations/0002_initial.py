# Generated by Django 4.1.3 on 2022-12-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property_app', '0001_initial'),
        ('owner_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_mod',
            name='owner_properties',
            field=models.ManyToManyField(blank=True, related_name='owner_properties', to='property_app.property_mod', verbose_name='Owner Properties'),
        ),
    ]
