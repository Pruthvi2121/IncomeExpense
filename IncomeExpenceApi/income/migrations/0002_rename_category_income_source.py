# Generated by Django 4.1.4 on 2023-01-15 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='category',
            new_name='source',
        ),
    ]