# Generated by Django 5.0.6 on 2024-05-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_result_total_marks_alter_result_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='Total_marks',
            field=models.IntegerField(default=0),
        ),
    ]