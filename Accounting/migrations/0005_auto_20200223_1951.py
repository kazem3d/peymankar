# Generated by Django 3.0.3 on 2020-02-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting', '0004_auto_20200217_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='description',
            field=models.TextField(null=True, verbose_name='توضیحات'),
        ),
    ]