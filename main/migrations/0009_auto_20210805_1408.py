# Generated by Django 3.2 on 2021-08-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210804_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestmeeting',
            name='date',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='requestmeeting',
            name='time',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='uploadtopic',
            name='supervisor',
            field=models.CharField(max_length=50),
        ),
    ]
