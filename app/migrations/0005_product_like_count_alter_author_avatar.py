# Generated by Django 4.2.10 on 2024-02-29 13:27

import app.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_productlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='', upload_to=app.utils.avatar_path),
        ),
    ]
