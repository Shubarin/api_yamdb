# Generated by Django 3.0.5 on 2021-02-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v0', '0003_auto_20210219_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, to='api_v0.Genre', verbose_name='Жанр'),
        ),
    ]
