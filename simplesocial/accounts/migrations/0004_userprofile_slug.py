# Generated by Django 3.1.4 on 2021-05-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210515_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=None, unique=True),
        ),
    ]
