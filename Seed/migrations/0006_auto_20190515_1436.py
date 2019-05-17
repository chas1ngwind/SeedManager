# Generated by Django 2.0.4 on 2019-05-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seed', '0005_auto_20190514_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generationinfo',
            name='role1',
        ),
        migrations.RemoveField(
            model_name='generationinfo',
            name='type1',
        ),
        migrations.RemoveField(
            model_name='seedinfo',
            name='selectRole',
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='generation',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='type',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='GenerationInfo',
        ),
        migrations.DeleteModel(
            name='SeedInfo',
        ),
    ]
