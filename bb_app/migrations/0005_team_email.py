# Generated by Django 3.0.2 on 2020-06-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_app', '0004_auto_20200613_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.URLField(default='yash', max_length=500),
            preserve_default=False,
        ),
    ]