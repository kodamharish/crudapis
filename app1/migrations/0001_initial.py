# Generated by Django 5.0.6 on 2024-05-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('empName', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pancard', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('labId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('patientId', models.IntegerField(editable=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('patientName', models.CharField(max_length=100)),
                ('testName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('patientName', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('doctorName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stdId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stdName', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
