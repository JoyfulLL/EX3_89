# Generated by Django 2.2.4 on 2023-10-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp89', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2023-10-17', max_length=20, verbose_name='出生日期'),
        ),
    ]
