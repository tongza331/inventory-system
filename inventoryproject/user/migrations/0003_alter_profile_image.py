# Generated by Django 4.0 on 2022-01-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/avatar.png', upload_to='Profile_Images'),
        ),
    ]