# Generated by Django 3.0.2 on 2020-06-12 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0003_campus_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventregistrationshackathon',
            old_name='grpLeaderContact',
            new_name='leaderContact',
        ),
        migrations.RenameField(
            model_name='eventregistrationshackathon',
            old_name='grpLeaderEmail',
            new_name='leaderEmail',
        ),
        migrations.RenameField(
            model_name='eventregistrationshackathon',
            old_name='grpLeaderName',
            new_name='leaderName',
        ),
        migrations.RenameField(
            model_name='eventregistrationshackathon',
            old_name='teamMembers',
            new_name='nameOfMembers',
        ),
        migrations.RenameField(
            model_name='eventregistrationshackathon',
            old_name='number',
            new_name='noOfMembers',
        ),
    ]