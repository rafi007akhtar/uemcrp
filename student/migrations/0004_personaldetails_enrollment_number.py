# Generated by Django 2.1.3 on 2019-04-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190409_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='enrollment_number',
            field=models.IntegerField(default=0),
        ),
    ]