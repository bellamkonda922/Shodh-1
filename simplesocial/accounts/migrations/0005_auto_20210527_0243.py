# Generated by Django 3.1.4 on 2021-05-26 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_group_selected_count'),
        ('accounts', '0004_userprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='job1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job1', to='groups.group'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job2', to='groups.group'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job3', to='groups.group'),
        ),
    ]