# Generated by Django 2.2.3 on 2019-07-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0002_poem_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='username',
            field=models.CharField(default='Анон', max_length=50),
        ),
    ]
