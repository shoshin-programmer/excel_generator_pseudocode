from django import forms
from . import models

class hrbpForm(forms.ModelForm):
    month_choices = (
        ("January", 'JANUARY'),
        ("February", 'FEBRUARY'),
        ("March",'MARCH' ),
        ("April",'APRIL'),
        ("May",'MAY' ),
        ("June",'JUNE' ),
        ("July",'JULY' ),
        ("August",'AUGUST' ),
        ("September",'SEPTEMBER' ),
        ( "October",'OCTOBER'),
        ("November",'NOVEMBER'),
        ( "December", 'DECEMBER')
    )
    month = forms.ChoiceField(choices=month_choices)
    excel_reference = forms.FileField(help_text='(Note: always clean data and do not change formatting)')

    month.widget.attrs['class'] = 'form-control mt-2 mb-3'    
    excel_reference.widget.attrs['class'] = 'form-control mt-2 mb-2'    

    class Meta:
        model = models.HRBP
        fields = ['month', 'excel_reference']


class genForm(forms.ModelForm):
    class Meta:
        model = models.HRBP
        fields = ['excel_reference']