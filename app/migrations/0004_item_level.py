# Generated by Django 4.0.6 on 2023-10-23 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_trade_secondary_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
