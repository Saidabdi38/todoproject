# Generated by Django 5.0.3 on 2024-03-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_register', '0007_alter_task_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completion',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Not Completed', 'Not Completed')], default='Not Completed', max_length=200),
        ),
    ]
