# Generated by Django 2.1.3 on 2019-04-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20190410_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetails',
            name='tenth_board_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='academicdetails',
            name='twelfth_board_percentage',
            field=models.IntegerField(default=0),
        ),
    ]
