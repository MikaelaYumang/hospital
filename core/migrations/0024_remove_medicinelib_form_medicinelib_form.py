# Generated by Django 4.2.4 on 2023-10-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_dosageform_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicinelib',
            name='form',
        ),
        migrations.AddField(
            model_name='medicinelib',
            name='form',
            field=models.ManyToManyField(null=True, to='core.dosageform'),
        ),
    ]