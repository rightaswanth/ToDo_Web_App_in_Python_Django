# Generated by Django 5.0.3 on 2024-03-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0002_task_delete_todo"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
    ]