# Generated by Django 3.1.2 on 2021-06-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_qualifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='qual_html',
            field=models.TextField(blank=True, default='', editable=False, null=True),
        ),
    ]
