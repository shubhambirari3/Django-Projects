# Generated by Django 5.1.4 on 2025-02-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_remove_task_created_at_remove_task_is_complete_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
