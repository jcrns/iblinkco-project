# Generated by Django 2.1.3 on 2019-01-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190107_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagram',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]