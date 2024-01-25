# Generated by Django 5.0.1 on 2024-01-22 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_users_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('party1_id', models.CharField(max_length=100)),
                ('party1_name', models.CharField(max_length=100)),
                ('party2_id', models.CharField(max_length=100)),
                ('party2_name', models.CharField(max_length=100)),
            ],
        ),
    ]
