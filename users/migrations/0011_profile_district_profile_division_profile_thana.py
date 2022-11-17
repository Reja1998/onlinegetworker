# Generated by Django 4.0.1 on 2022-10-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_busy'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(blank=True, choices=[('মানিকগঞ্জ', 'মানিকগঞ্জ'), ('টাঙ্গাইল', 'টাঙ্গাইল'), ('ফরিদপুর', 'ফরিদপুর'), ('গাজিপুর', 'গাজিপুর'), ('রাজবারি', 'রাজবারি'), ('পাবনা', 'পাবনা'), ('নাটোর', 'নাটোর'), ('চাপাইনবাবগঞ্জ', 'চাপাইনবাবগঞ্জ'), ('বগুরা', 'বগুরা')], max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='division',
            field=models.CharField(blank=True, choices=[('ঢাকা', 'ঢাকা'), ('রাজশাহী', 'রাজশাহী'), ('যশোর', 'যশোর')], max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='thana',
            field=models.CharField(blank=True, choices=[('মানিকগঞ্জ সদর', 'মানিকগঞ্জ সদর'), ('হরিরামপুর', 'হরিরামপুর'), ('শিবালয়', 'শিবালয়'), ('ঘিয়র', 'ঘিয়র'), ('সিংগাইর', 'সিংগাইর'), ('পাবনা সদর উপজেলা', 'পাবনা সদর উপজেলা'), ('বগুরা', 'বগুরা')], max_length=200),
        ),
    ]