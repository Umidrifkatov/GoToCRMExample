# Generated by Django 2.2.3 on 2019-08-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_student_photo_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.FileField(null=True, upload_to='avatars'),
        ),
    ]
