# Generated by Django 3.2.7 on 2021-10-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborlyUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborlyuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
