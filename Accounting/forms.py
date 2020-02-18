from django import forms

class SearchForm(forms.Form):
    record_name=forms.CharField(label='جستجوی رکورد',required=False)