# Generated by Django 3.2.10 on 2023-05-10 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0005_remove_department_image1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='DepartmentName',
            new_name='Name',
        ),
    ]
