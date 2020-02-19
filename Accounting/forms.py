from django import forms
from Accounting.models import Project

class SearchForm(forms.Form):
    record_name=forms.CharField(label='عنوان',required=False)
    project_name=forms.ModelChoiceField(label='نام پروژه',
                queryset=Project.objects.all(),required=False)
    max_price=forms.IntegerField(label='بیشترین قیمت',required=False)
    min_price=forms.IntegerField(label='کمترین قیمت',required=False)
    