# Generated by Django 3.1.2 on 2020-11-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersignup',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]