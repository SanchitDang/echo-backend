# Generated by Django 5.0.3 on 2024-05-16 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_banner_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
