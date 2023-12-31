# Generated by Django 4.2.4 on 2023-10-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_contactform_address_remove_contactform_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='medicinelib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='medicine')),
                ('description', models.TextField()),
                ('uses', models.TextField()),
            ],
        ),
    ]
