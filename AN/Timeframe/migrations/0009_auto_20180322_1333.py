# Generated by Django 2.0.3 on 2018-03-22 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Timeframe', '0008_component_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'ordering': ('completed', '-created')},
        ),
    ]