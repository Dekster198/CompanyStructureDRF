# Generated by Django 5.1.2 on 2024-10-10 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('post', models.CharField(max_length=64)),
                ('salary', models.IntegerField()),
                ('age', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='structure.department', unique=True)),
            ],
        ),
    ]
