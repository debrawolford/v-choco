# Generated by Django 3.1.2 on 2020-11-15 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
