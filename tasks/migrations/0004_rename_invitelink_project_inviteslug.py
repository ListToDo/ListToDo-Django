# Generated by Django 3.2.8 on 2021-11-01 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_project_invitelink'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='inviteLink',
            new_name='inviteSlug',
        ),
    ]
