# Generated by Django 2.0.4 on 2019-05-15 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seed', '0008_auto_20190515_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailinfo',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='detailinfo',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Seed.RoleInfo'),
        ),
    ]
