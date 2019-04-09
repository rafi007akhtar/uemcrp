# Generated by Django 2.1.3 on 2019-04-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_profilepic_enrollment_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_number', models.IntegerField(default=0)),
                ('email_id', models.EmailField(max_length=50)),
                ('mobile_number', models.IntegerField(max_length=15)),
                ('country', models.CharField(default='India', max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField(max_length=6)),
                ('address', models.CharField(max_length=200)),
                ('permanent_address', models.CharField(max_length=200)),
                ('guardian_email', models.EmailField(max_length=254)),
                ('guardian_mobile', models.IntegerField()),
                ('guardian_relation', models.CharField(max_length=20)),
            ],
        ),
    ]
