# Generated by Django 2.1.3 on 2019-03-20 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20190307_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followopperation',
            name='number_of_followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='number_of_followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='number_of_following',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='instagram',
            name='number_of_post',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='likeopperation',
            name='number_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='number_of_followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='number_of_following',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='twitter',
            name='number_of_post',
            field=models.IntegerField(default=0),
        ),
    ]