# Generated by Django 3.2 on 2021-08-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210805_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendinvite',
            name='student',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sendinvite',
            name='supervisor',
            field=models.CharField(max_length=50),
        ),
    ]
