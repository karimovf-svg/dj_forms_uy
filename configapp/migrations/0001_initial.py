# Generated by Django 5.1.6 on 2025-03-04 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='student')),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_bool', models.BooleanField(default=True)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.fanlar')),
            ],
            options={
                'verbose_name': 'NEW',
                'verbose_name_plural': 'NEWS',
                'ordering': ['-created_ed'],
            },
        ),
    ]
