# Generated by Django 3.1.2 on 2020-11-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201115_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='town_or_city',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='county',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Gender'), (1, 'Male'), (2, 'Female'), (3, 'Other')], default=0, null=True),
        ),
    ]