# Generated by Django 4.1.3 on 2023-01-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeshistory',
            name='his_image',
            field=models.CharField(blank=True, db_column='pathToFile', max_length=500, null=True),
        ),
    ]