# Generated by Django 2.2.2 on 2020-04-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iportal', '0004_auto_20200415_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='brief',
            field=models.CharField(default='Need a person for this position', max_length=40),
            preserve_default=False,
        ),
    ]
