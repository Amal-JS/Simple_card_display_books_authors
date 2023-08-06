# Generated by Django 4.2.3 on 2023-07-11 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField()),
                ('no_of_awards', models.IntegerField()),
                ('dob', models.DateField()),
                ('author_image', models.ImageField(upload_to='author_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('release_date', models.DateField()),
                ('book_image', models.ImageField(upload_to='book_images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.author')),
                ('genre', models.ManyToManyField(to='library_app.genre')),
            ],
        ),
    ]