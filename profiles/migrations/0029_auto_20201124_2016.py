# Generated by Django 3.1.2 on 2020-11-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0028_auto_20201124_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='initials',
            field=models.CharField(max_length=20),
        ),
    ]
