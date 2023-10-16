# Generated by Django 4.2.4 on 2023-10-16 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_contactform_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicinedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.TextField()),
                ('usage_info', models.TextField()),
                ('medicine', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='core.medicinelib')),
            ],
        ),
    ]