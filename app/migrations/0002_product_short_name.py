# Generated by Django 3.0 on 2023-09-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_name',
            field=models.CharField(default='Energy Saving', max_length=20, verbose_name='short_name'),
        ),
    ]