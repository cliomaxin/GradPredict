# Generated by Django 5.0.7 on 2024-08-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_remove_studentuser_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='mode_of_learning',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='', null=True, upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='program_entrance',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='student_id',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
