# Generated by Django 4.0.1 on 2022-09-21 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='title',
        ),
    ]
