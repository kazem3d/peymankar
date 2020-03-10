from django import forms
from Accounting.models import Project,recording
from django.core.exceptions import ValidationError

class SearchForm(forms.Form):

    NOTING=None
    EXPENSE='1'
    INCOME='2'

    types_choice=(
        
        (EXPENSE,'خرج کرد'),
        
        (INCOME,'درآمد'),
        (NOTING,'-----')
        
    )



    record_name=forms.CharField(label='عنوان',required=False)
    project_name=forms.ModelChoiceField(label='نام پروژه',
                queryset=Project.objects.all(),required=False)
    max_price=forms.IntegerField(label='بیشترین قیمت',min_value=0,required=False)
    min_price=forms.IntegerField(label='کمترین قیمت',min_value=0,required=False)
    type_of=forms.ChoiceField(label='نوع',choices=types_choice)
                               


class RegisterRecordForm(forms.ModelForm):
    class Meta:
        model=recording
        exclude=[]
        

    # def clean_unit_price(self):
    #     unit_price=self.cleaned_data.get('unit_price')
    #     if unit_price % 1000 != 0:
    #         raise ValidationError('مقداردرست نیست')
    #     else:
    #         return unit_price


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=[]
