from django import forms
from django.forms.widgets import NumberInput
import datetime


BIRTH_YEAR_CHOICES = ['2000', '2001', '2002']
FAVORITE_PROGRAMMING_LANGUAGE = [
    ('JS', 'JS'),
    ('C++', 'C++'),
    ('Python', 'Python'),
]

class ExampleForm(forms.Form):
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}),initial=datetime.date.today,required=False)
    name = forms.CharField(label="Enter your name",initial="Mor nam...")
    national_id = forms.IntegerField(help_text = "Enter 6 digit id number",required=False) 
    father_name = forms.CharField(label="Baper nam ki?",initial="omuk")
    Address = forms.CharField(label="Bari kone?")
    email = forms.EmailField(label="Enter your mail ",required=False)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),required=False)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_PROGRAMMING_LANGUAGE,required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),required=False)
    agree = forms.BooleanField()

