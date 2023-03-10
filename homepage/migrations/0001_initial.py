# Generated by Django 4.1.4 on 2022-12-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksHolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=255)),
                ('book_link', models.URLField()),
                ('book_image', models.FileField(upload_to='image')),
            ],
        ),
    ]
