# Generated by Django 2.2.6 on 2019-11-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0005_variable'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='type_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
