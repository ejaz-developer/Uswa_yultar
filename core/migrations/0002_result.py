# Generated by Django 5.0.6 on 2024-05-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_class', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField(max_length=100)),
                ('student_section', models.CharField(max_length=100)),
            ],
        ),
    ]
