# Generated by Django 5.0.1 on 2024-01-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('company_name', models.CharField(max_length=500)),
                ('company_size', models.CharField(max_length=500)),
                ('manufacturer_category', models.CharField(max_length=500)),
                ('adhaar_number', models.CharField(max_length=200)),
            ],
        ),
    ]
