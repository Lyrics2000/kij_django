# Generated by Django 4.1.4 on 2023-01-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_kijabeserivices'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaystoreBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
    ]
