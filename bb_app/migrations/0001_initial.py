# Generated by Django 3.0.2 on 2020-06-12 15:00

import bb_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/Campus_Companies')),
                ('students', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('date', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('details', models.TextField()),
                ('eventType', models.CharField(choices=[('Panel Session', 'Panel Session'), ('Workshop', 'Workshop'), ('Hackathon', 'Hackathon'), ('FunLearning', 'FunLearning')], default='Panel Session', max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sponsers')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=bb_app.models.get_path_team)),
                ('name', models.CharField(max_length=255)),
                ('post', models.CharField(max_length=100)),
                ('facebook', models.URLField(max_length=500)),
                ('linkedin', models.URLField(max_length=500)),
                ('year', models.IntegerField(help_text='Enter in this format:2020')),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistrationsHackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grpLeaderName', models.CharField(max_length=100)),
                ('grpLeaderEmail', models.EmailField(max_length=254)),
                ('grpLeaderContact', models.IntegerField()),
                ('college', models.CharField(default='K. J. Somaiya College of Engineering', max_length=255)),
                ('number', models.IntegerField()),
                ('teamMembers', models.TextField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrationsHackathon', to='bb_app.Events')),
            ],
        ),
        migrations.CreateModel(
            name='EventRegistrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('college', models.CharField(default='K. J. Somaiya College of Engineering', max_length=255)),
                ('branch', models.CharField(max_length=100)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='bb_app.Events')),
            ],
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moreImages', models.ImageField(blank=True, null=True, upload_to=bb_app.models.get_path_events)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moreImages', to='bb_app.Events')),
            ],
        ),
    ]