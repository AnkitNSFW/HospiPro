# Generated by Django 4.2.5 on 2023-09-28 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_db_doctor_medical_license_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_doctor',
            name='availability',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='db_doctor',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='db_doctor',
            name='specialty',
            field=models.CharField(max_length=50),
        ),
    ]
