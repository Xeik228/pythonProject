# Generated by Django 4.1.1 on 2022-10-04 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0021_alter_actor_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actors',
        ),
    ]
