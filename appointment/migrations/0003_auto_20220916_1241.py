# Generated by Django 3.2.15 on 2022-09-16 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20220916_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='class_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ClassName',
        ),
    ]
