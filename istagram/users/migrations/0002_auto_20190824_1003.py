# Generated by Django 2.2.4 on 2019-08-24 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='peofile_image',
            new_name='profile_image',
        ),
    ]
