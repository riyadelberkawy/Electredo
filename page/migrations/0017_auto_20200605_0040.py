# Generated by Django 3.0.6 on 2020-06-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0016_auto_20200605_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.CharField(default='افلام', max_length=100),
        ),
        migrations.AddField(
            model_name='series',
            name='category',
            field=models.CharField(default='مسلسلات', max_length=100),
        ),
    ]
