# Generated by Django 2.1.5 on 2019-01-13 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190113_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='vivechak',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='main.Vivechak'),
        ),
    ]
