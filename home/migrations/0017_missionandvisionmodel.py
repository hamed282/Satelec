# Generated by Django 5.1.1 on 2024-10-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_aboutpagemodel_alter_blogmodel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissionAndVisionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='img/aboutus')),
                ('title', models.CharField(max_length=128)),
                ('subtitle', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
                ('title_about', models.CharField(max_length=128)),
                ('subtitle_about', models.CharField(max_length=128)),
                ('column1_title', models.CharField(max_length=128)),
                ('column1_description', models.TextField(max_length=512)),
                ('column1_link', models.CharField(max_length=512)),
                ('column2_title', models.CharField(max_length=128)),
                ('column2_description', models.TextField(max_length=512)),
                ('column2_link', models.CharField(max_length=512)),
            ],
        ),
    ]