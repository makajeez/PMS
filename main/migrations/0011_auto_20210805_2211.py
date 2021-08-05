# Generated by Django 3.2 on 2021-08-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210805_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadproposal',
            name='proposal_file',
            field=models.FileField(default='-', upload_to='files'),
        ),
        migrations.AlterField(
            model_name='uploadproposal',
            name='student',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='uploadproposal',
            name='supervisor',
            field=models.CharField(max_length=30),
        ),
    ]
