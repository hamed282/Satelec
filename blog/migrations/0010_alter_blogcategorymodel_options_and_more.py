# Generated by Django 5.1.1 on 2024-10-08 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogmodel_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategorymodel',
            options={'verbose_name': 'Blog Category', 'verbose_name_plural': 'Blog Categories'},
        ),
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]