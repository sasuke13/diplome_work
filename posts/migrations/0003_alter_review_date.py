# Generated by Django 5.1.2 on 2024-11-05 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_textbesidetheimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
