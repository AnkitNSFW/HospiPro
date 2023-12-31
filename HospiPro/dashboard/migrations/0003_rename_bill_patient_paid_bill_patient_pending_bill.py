# Generated by Django 4.2.5 on 2023-10-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_patient_bill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='bill',
            new_name='paid_bill',
        ),
        migrations.AddField(
            model_name='patient',
            name='pending_bill',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
