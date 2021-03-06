# Generated by Django 3.0.6 on 2020-05-30 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeID', models.CharField(max_length=200)),
                ('EmployeeName', models.CharField(max_length=200)),
                ('EmployeeDesignation', models.CharField(max_length=200)),
                ('Group', models.CharField(max_length=200)),
                ('SiC', models.DateTimeField(verbose_name='date published')),
                ('HireDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
