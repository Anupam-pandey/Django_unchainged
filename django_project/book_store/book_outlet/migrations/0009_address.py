# Generated by Django 3.2.4 on 2021-06-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0008_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50)),
                ('postal', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
