# Generated by Django 4.0.4 on 2022-10-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
