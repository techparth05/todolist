# Generated by Django 3.2.7 on 2021-11-25 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed']},
        ),
    ]
