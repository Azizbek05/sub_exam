# Generated by Django 5.0.4 on 2024-05-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tag',
            field=models.CharField(choices=[('phone', 'phone'), ('apliances', 'apliances'), ('laptop', 'laptop')], default=-1, max_length=50),
            preserve_default=False,
        ),
    ]
