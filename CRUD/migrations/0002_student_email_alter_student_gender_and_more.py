# Generated by Django 4.1.7 on 2023-03-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
