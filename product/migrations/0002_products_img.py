# Generated by Django 5.0.4 on 2024-04-29 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default=-1, upload_to=''),
            preserve_default=False,
        ),
    ]
