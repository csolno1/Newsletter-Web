# Generated by Django 2.0.6 on 2018-07-10 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_readrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readrecord',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]