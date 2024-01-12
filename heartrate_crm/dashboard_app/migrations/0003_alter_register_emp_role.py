# Generated by Django 5.0.1 on 2024-01-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0002_register_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_emp',
            name='role',
            field=models.CharField(choices=[('super_admin', 'super_admin'), ('admin', 'admin'), ('manager', 'manager'), ('operation', 'operation'), ('hr', 'hr'), ('agent', 'agent')], default='', max_length=24),
        ),
    ]