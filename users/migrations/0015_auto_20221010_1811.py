# Generated by Django 3.2.4 on 2022-10-10 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20221010_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='thana',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='union',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='village',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]