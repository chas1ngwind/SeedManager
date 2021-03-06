# Generated by Django 2.0.4 on 2019-05-14 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generationinfo',
            name='selectRole',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Seed.RoleInfo'),
        ),
        migrations.AddField(
            model_name='generationinfo',
            name='selectType',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Seed.SeedInfo'),
        ),
        migrations.AddField(
            model_name='seedinfo',
            name='selectRole',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Seed.RoleInfo'),
        ),
    ]
