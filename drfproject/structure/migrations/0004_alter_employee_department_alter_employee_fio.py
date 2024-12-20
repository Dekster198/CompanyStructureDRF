# Generated by Django 5.1.2 on 2024-10-10 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_alter_employee_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='structure.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fio',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]
