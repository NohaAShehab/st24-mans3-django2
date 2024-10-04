# Generated by Django 5.1.1 on 2024-10-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
