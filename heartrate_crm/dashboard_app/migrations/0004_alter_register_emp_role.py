# Generated by Django 5.0.1 on 2024-01-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0003_alter_register_emp_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_emp',
            name='role',
            field=models.CharField(choices=[('super_admin', 'super_admin'), ('admin', 'admin'), ('manager', 'manager'), ('operation', 'operation'), ('hr', 'hr'), ('agent', 'agent')], default='agent', max_length=24),
        ),
    ]
