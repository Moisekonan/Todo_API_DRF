# Generated by Django 4.2.7 on 2023-11-08 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitem',
            options={'verbose_name': 'Todo Item', 'verbose_name_plural': 'Todo Items'},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'Todo List', 'verbose_name_plural': 'Todo Lists'},
        ),
    ]
