# Generated by Django 4.1.13 on 2024-08-05 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_studentuser_username_alter_studentuser_gender_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
