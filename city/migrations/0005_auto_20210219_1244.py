# Generated by Django 3.1.6 on 2021-02-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_auto_20210219_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название города'),
        ),
        migrations.AlterField(
            model_name='street',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Название улицы'),
        ),
    ]
