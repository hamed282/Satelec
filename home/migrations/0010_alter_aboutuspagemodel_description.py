# Generated by Django 5.1.1 on 2024-10-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_aboutpagemodel_aboutuspagemodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspagemodel',
            name='description',
            field=models.TextField(max_length=256),
        ),
    ]
