# Generated by Django 5.0.1 on 2024-01-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0005_alter_register_emp_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_emp',
            name='role',
            field=models.CharField(max_length=24),
        ),
    ]
