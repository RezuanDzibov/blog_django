# Generated by Django 3.2.6 on 2021-08-25 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialLink',
        ),
    ]