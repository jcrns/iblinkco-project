# Generated by Django 2.1.3 on 2019-01-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='contactus',
            name='message',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
