# Generated by Django 3.0.6 on 2020-05-30 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200530_1805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Employees',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='HireDate',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='SiC',
        ),
    ]
