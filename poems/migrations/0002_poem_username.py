# Generated by Django 2.2.3 on 2019-07-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poem',
            name='username',
            field=models.TextField(default='Анон'),
            preserve_default=False,
        ),
    ]
