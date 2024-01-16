# Generated by Django 5.0.1 on 2024-01-13 13:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_mainmenuitems_delete_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', ckeditor.fields.RichTextField()),
                ('about', ckeditor.fields.RichTextField()),
                ('twitter_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('copyright_text', ckeditor.fields.RichTextField()),
            ],
        ),
    ]