# Generated by Django 2.0.3 on 2018-03-22 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Timeframe', '0006_auto_20180322_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]