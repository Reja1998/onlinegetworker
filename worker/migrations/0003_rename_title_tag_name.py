# Generated by Django 4.0.1 on 2022-09-21 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_rename_name_tag_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='title',
            new_name='name',
        ),
    ]
