# Generated by Django 3.2.8 on 2022-01-21 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tasks_api.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('inviteSlug', models.SlugField(blank=True, null=True)),
                ('archive', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('schedule', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_owner', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subprojects', to='tasks_api.project')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='users.team')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('archive', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='tasks_api.project')),
            ],
            options={
                'ordering': ['position'],
                'unique_together': {('project', 'position')},
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8']], max_length=1, null=True)),
                ('priority', models.CharField(blank=True, choices=[['1', 'Priority 1'], ['2', 'Priority 2'], ['3', 'Priority 3'], ['4', 'Priority 4'], ['5', 'Priority 5']], max_length=1, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('schedule', models.DateTimeField(blank=True, null=True)),
                ('every', models.CharField(blank=True, choices=[('0', 'EveryDay'), ('1', 'Sunday'), ('2', 'Monday'), ('3', 'Tuesday'), ('4', 'Wednesday'), ('5', 'Thursday'), ('6', 'Friday'), ('7', 'Saturday')], max_length=1, null=True)),
                ('completedDate', models.DateTimeField(blank=True, null=True)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('label', models.ManyToManyField(blank=True, related_name='tasks', to='tasks_api.Label')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_creator', to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks_api.section')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='tasks_api.task')),
            ],
            options={
                'ordering': ['position'],
                'unique_together': {('section', 'position')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to=tasks_api.utils.upload_file)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks_api.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tasks_api.task')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('C', 'Created'), ('U', 'Updated'), ('D', 'Deleted')], max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity', to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity', to='tasks_api.comment')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='tasks_api.project')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity', to='tasks_api.section')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activity', to='tasks_api.task')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'], ['8', '8']], max_length=1, null=True)),
                ('background', models.ImageField(blank=True, null=True, upload_to=tasks_api.utils.upload_file)),
                ('label', models.ManyToManyField(blank=True, related_name='projects', to='tasks_api.Label')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='tasks_api.project')),
            ],
            options={
                'unique_together': {('owner', 'project'), ('owner', 'position')},
            },
        ),
    ]
