# Generated by Django 4.2.4 on 2023-10-10 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_uses_medicinelib_side_effects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicinelib',
            options={'ordering': ['name']},
        ),
    ]
