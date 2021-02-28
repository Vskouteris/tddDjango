# Generated by Django 3.1.6 on 2021-02-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210228_0641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='parameter',
        ),
        migrations.RemoveField(
            model_name='parameter',
            name='offer',
        ),
        migrations.AddField(
            model_name='offer',
            name='parameters',
            field=models.ManyToManyField(to='backend.Parameter'),
        ),
        migrations.AddField(
            model_name='parameter',
            name='details',
            field=models.ManyToManyField(to='backend.Detail'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='category',
            field=models.CharField(choices=[('HOURS', 'HOURS'), ('DIMENSIONS', 'DIMENSIONS'), ('TYPE', 'TYPE'), ('EXTRA', 'EXTRA'), ('ONTOULE', 'ONTOULE')], default=('HOURS', 'HOURS'), max_length=255),
        ),
    ]
