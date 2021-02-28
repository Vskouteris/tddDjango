# Generated by Django 3.1.6 on 2021-02-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210228_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='parameters',
            field=models.ManyToManyField(help_text='choose all parameters affecting the offer', to='backend.Parameter'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='details',
            field=models.ManyToManyField(help_text='choose all Details affecting the parameter', to='backend.Detail'),
        ),
    ]
