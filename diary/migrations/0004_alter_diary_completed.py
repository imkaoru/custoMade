# Generated by Django 3.2.9 on 2021-12-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20211204_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='completed',
            field=models.CharField(default='unchecked', max_length=10),
        ),
    ]