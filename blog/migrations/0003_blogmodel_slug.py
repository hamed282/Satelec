# Generated by Django 5.1.1 on 2024-09-28 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcategorymodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
