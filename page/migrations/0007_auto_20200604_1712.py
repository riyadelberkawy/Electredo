# Generated by Django 3.0.6 on 2020-06-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20200604_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='download_url',
            field=models.CharField(default='#', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='download_url',
            field=models.CharField(default='#', max_length=300, null=True),
        ),
    ]
