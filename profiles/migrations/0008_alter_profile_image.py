# Generated by Django 5.0.4 on 2024-05-21 23:43

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='profiles/default_pfp/default.jpg', upload_to='profiles'),
        ),
    ]
