# Generated by Django 3.2.7 on 2021-10-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
