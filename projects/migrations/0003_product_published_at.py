# Generated by Django 5.0.2 on 2024-02-12 18:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='published_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
