# Generated by Django 2.1.3 on 2019-01-06 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20190105_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]