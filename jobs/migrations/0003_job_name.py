# Generated by Django 3.2.8 on 2021-10-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_jobs_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default='website', max_length=100),
            preserve_default=False,
        ),
    ]
