# Generated by Django 5.1.2 on 2024-11-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='senha',
            field=models.CharField(default=123, max_length=100),
            preserve_default=False,
        ),
    ]
