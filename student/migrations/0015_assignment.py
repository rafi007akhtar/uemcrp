# Generated by Django 2.1.3 on 2019-04-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(default=0)),
                ('section', models.CharField(max_length=2)),
                ('assignment', models.FileField(upload_to='')),
            ],
        ),
    ]
