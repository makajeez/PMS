# Generated by Django 3.2 on 2021-08-04 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210804_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='Buhari Ahmed Alhassan', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default='CST-16-CO-00543', max_length=50),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='fullname',
            field=models.CharField(default='Prof F U Ambursa', max_length=50),
        ),
        migrations.AddField(
            model_name='supervisor',
            name='username',
            field=models.CharField(default='fua.isc@buk.edu.ng', max_length=50),
        ),
    ]