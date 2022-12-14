# Generated by Django 3.2.15 on 2022-09-16 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20220916_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.teacher')),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='appointment.classname'),
        ),
    ]
