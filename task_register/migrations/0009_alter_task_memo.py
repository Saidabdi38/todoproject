# Generated by Django 5.0.3 on 2024-03-17 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_register', '0008_alter_task_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='memo',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
