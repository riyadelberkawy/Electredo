# Generated by Django 3.0.6 on 2020-06-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_remove_film_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='cate',
            field=models.CharField(default='افلام', max_length=100),
        ),
    ]
