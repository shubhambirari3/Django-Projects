# Generated by Django 5.1.5 on 2025-01-30 09:49

import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(max_length=1000)),
                ('image', models.ImageField(upload_to='blog_images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
