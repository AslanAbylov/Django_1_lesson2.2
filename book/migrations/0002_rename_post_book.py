# Generated by Django 4.0.1 on 2022-01-10 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Book',
        ),
    ]