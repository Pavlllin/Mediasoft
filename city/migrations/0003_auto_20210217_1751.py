# Generated by Django 3.1.6 on 2021-02-17 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_auto_20210217_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='street',
            old_name='street',
            new_name='title',
        ),
    ]
