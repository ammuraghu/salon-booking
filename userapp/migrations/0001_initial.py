# Generated by Django 5.1.4 on 2025-02-07 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=23)),
                ('Age', models.IntegerField()),
                ('Phn', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=130)),
                ('Pincode', models.IntegerField()),
                ('Password', models.CharField(max_length=23)),
                ('Repass', models.CharField(max_length=23)),
            ],
        ),
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(default='9AM-1PM', max_length=20)),
                ('Note', models.CharField(max_length=250)),
                ('ServiceID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.services')),
                ('userreg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.reg')),
            ],
        ),
    ]
