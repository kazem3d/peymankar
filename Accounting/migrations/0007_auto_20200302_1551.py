# Generated by Django 3.0.3 on 2020-03-02 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounting', '0006_remove_recording_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cost',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='مبلغ قرارداد'),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ قرارداد'),
        ),
        migrations.AddField(
            model_name='project',
            name='master',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نام کارفرما '),
        ),
        migrations.AddField(
            model_name='project',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='شماره قرارداد'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'در دست اجرا'), ('2', 'پیش نویس'), ('3', 'تحویل موقت'), ('4', 'تحویل قطعی'), ('5', 'تعلیق')], max_length=15, null=True, verbose_name='وضعیت قرارداد'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, verbose_name='عنوان پروژه'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='amount',
            field=models.BigIntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='recording',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات'),
        ),
    ]