# Generated by Django 4.1.1 on 2022-09-07 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_med', '0005_alter_news_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='create_time',
            new_name='create_date',
        ),
    ]