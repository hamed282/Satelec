# Generated by Django 5.1.1 on 2024-10-08 05:52

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_aboutuspagemodel_banner_alt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuspagemodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='commitmentmodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='commoditiestradingmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='customercentricfocusmodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='electricalequipmentmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='healthcareproductmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='heavymachinerymodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='description_blog',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='homemodel',
            name='description_service',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='missionandvisionmodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='solarsystemmodel',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='sustainabilityinitiativemodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='whatwedomodel',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]