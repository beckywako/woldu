# Generated by Django 4.1.3 on 2022-11-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='heart.png', null=True, upload_to='profile'),
        ),
    ]
