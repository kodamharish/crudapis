# Generated by Django 5.0.6 on 2024-06-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeIDSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_id', models.IntegerField(default=0)),
            ],
        ),
    ]
