# Generated by Django 3.1.1 on 2020-09-30 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200930_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationdetail',
            name='req',
            field=models.CharField(default='', max_length=100),
        ),
    ]
