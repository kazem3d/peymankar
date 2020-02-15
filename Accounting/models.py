from django.db import models

class recording(models.Model):
    
    class Meta:

        verbose_name="ثبت دخل و خرج"
        verbose_name_plural="ثبت دخل و خرج"
    

    types_choice=[
        ('1','خرج کرد'),
        ('2','درآمد')
    ]

    types=models.CharField('نوع',choices=types_choice,max_length=10)
    title=models.CharField('عنوان',max_length=100)
    amount=models.IntegerField('تعداد')
    unit_price=models.IntegerField('مبلغ واحد')
    total_price=models.IntegerField('مبلغ کل')
    date=models.DateField('تاریخ')
    description=models.TextField('توضیحات')

