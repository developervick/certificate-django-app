# Generated by Django 4.2.3 on 2023-07-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_certificate_certificate_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate_model',
            name='certificate_id',
            field=models.CharField(max_length=250),
        ),
    ]
