# Generated by Django 2.1.3 on 2019-04-17 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='enrollment_number',
            new_name='semester',
        ),
    ]
