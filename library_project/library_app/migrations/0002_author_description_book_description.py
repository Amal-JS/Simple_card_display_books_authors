# Generated by Django 4.2.3 on 2023-07-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default='no data available'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
