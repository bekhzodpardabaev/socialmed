# Generated by Django 4.1.1 on 2022-09-09 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_med', '0004_alter_apply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social_med.services'),
            preserve_default=False,
        ),
    ]
