# Generated by Django 5.1.2 on 2024-11-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_review_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewplugin',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]