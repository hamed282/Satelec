# Generated by Django 5.1.1 on 2024-10-10 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_contactuspagemodel_map_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspagemodel',
            name='column1_description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='aboutuspagemodel',
            name='column2_description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='addcommitmentmodel',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='addcustomercentricfocusmodel',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='addsustainabilityinitiativemodel',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='addwhatwedomodel',
            name='description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='missionandvisionmodel',
            name='column1_description',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='missionandvisionmodel',
            name='column2_description',
            field=models.TextField(max_length=2000),
        ),
    ]