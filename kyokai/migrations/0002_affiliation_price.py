# Generated by Django 2.1.2 on 2018-10-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyokai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliation',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Price'),
        ),
    ]
