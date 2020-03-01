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
    

    types_choice=[
        ('1','خرج کرد'),
        ('2','درآمد')
    ]

    types=models.CharField('نوع',choices=types_choice,max_length=10)
    project=models.ForeignKey('Project',on_delete=models.PROTECT,verbose_name='نام پروژه',null=True)
    title=models.CharField('عنوان',max_length=100)
    amount=models.BigIntegerField('تعداد')
    unit_price=models.BigIntegerField('مبلغ واحد')
    # total_price=models.BigIntegerField('مبلغ کل')
    
    date=models.DateField('تاریخ')
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

    name=models.CharField('عنوان پروژه', max_length=50)

    def __str__(self):
        return '{}'.format(self.name)