# Generated by Django 3.1.4 on 2021-06-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='branch',
            field=models.CharField(choices=[('bt', 'Biotech'), ('ch', 'Chemical'), ('cse', 'Computer Science'), ('mnc', 'Mathematics'), ('ep', 'Engineering Physics'), ('ece', 'Electronics'), ('ee', 'Electrical'), ('me', 'Mechanical'), ('cv', 'Civil'), ('cst', 'CST'), ('na', 'Not Applicable')], default='na', max_length=255),
        ),
    ]
