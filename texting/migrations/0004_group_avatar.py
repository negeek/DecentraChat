# Generated by Django 3.2.12 on 2022-10-19 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texting', '0003_deletedmessages'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='avatar',
            field=models.FileField(default='default.jpg', upload_to='profile_images/'),
        ),
    ]