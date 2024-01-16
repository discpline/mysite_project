# Generated by Django 5.0.1 on 2024-01-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_menuitem_delete_mainmenuitems'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='menu item')),
                ('slug', models.SlugField(verbose_name='url')),
                ('url', models.CharField(blank=True, max_length=100)),
                ('is_anchor', models.BooleanField(default=False)),
                ('is_manager_only', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
