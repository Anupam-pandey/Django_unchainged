# Generated by Django 3.2.4 on 2021-06-19 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='ratings',
            new_name='rating',
        ),
    ]
