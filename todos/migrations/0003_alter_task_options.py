# Generated by Django 4.1.3 on 2022-11-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20210219_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date_created']},
        ),
    ]