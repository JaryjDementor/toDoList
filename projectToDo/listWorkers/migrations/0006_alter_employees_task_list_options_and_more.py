# Generated by Django 4.0.4 on 2022-05-03 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listWorkers', '0005_alter_employees_task_list_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees_task_list',
            options={'ordering': ['id'], 'verbose_name': 'Employees_Task_List', 'verbose_name_plural': 'Employees_Task_List'},
        ),
        migrations.RemoveField(
            model_name='employees_task_list',
            name='status',
        ),
    ]
