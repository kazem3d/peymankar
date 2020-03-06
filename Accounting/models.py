from django.db import models

from django.db.models import F
class AnnotationManager(models.Manager):

    def __init__(self, **kwargs):
        super().__init__()
        self.annotations = kwargs

    def get_queryset(self):
        return super().get_queryset().annotate(**self.annotations)


class recording(models.Model):
    
    class Meta:

        verbose_name="ثبت دخل و خرج"
        verbose_name_plural="ثبت دخل و خرج"
    
    EXPENSE='1'
    INCOME='2'

    types_choice=(
        (EXPENSE,'خرج کرد'),
        (INCOME,'درآمد')
    )

    types=models.CharField('نوع',choices=types_choice,max_length=10)
    project=models.ForeignKey('Project',on_delete=models.PROTECT,verbose_name='نام پروژه',null=True)
    title=models.CharField('عنوان',max_length=100)
    amount=models.BigIntegerField('تعداد')
    unit_price=models.BigIntegerField('مبلغ واحد')
    # total_price=models.BigIntegerField('مبلغ کل')
    
    date=models.DateField('تاریخ',null=True,blank=True)
    description=models.TextField('توضیحات',null=True,blank=True)

    _total_price=None

    objects = AnnotationManager(

        total_price=F('amount') * F('unit_price')
    )



    def __str__(self):
        return '{}    {}  {}' .format(self.title,self.total_price,self.date)


class Project(models.Model):

    class Meta:
        verbose_name="پروژه"
        verbose_name_plural="پروژه ها"

    status_choise=[
        ('1','در دست اجرا'),
        ('2','پیش نویس'),
        ('3','تحویل موقت'),
        ('4','تحویل قطعی'),
        ('5','تعلیق')
    ]

    name=models.CharField('عنوان پروژه', max_length=50)
    number=models.CharField('شماره قرارداد',max_length=50,null=True,blank=True)
    date=models.DateField('تاریخ قرارداد',null=True,blank=True)
    cost=models.BigIntegerField('مبلغ قرارداد',null=True,blank=True)
    master=models.CharField('نام کارفرما ',max_length=50,null=True,blank=True)
    status=models.CharField('وضعیت قرارداد',choices=status_choise,null=True,blank=True,max_length=15)
    
    
    def __str__(self):
        return '{}'.format(self.name)