# Generated by Django 2.1.3 on 2019-04-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20190410_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetails',
            name='tenth_school_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='academicdetails',
            name='twelfth_school_name',
            field=models.CharField(max_length=100),
        ),
    ]