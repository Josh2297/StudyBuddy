from django import forms
import pdfplumber
import re
from django.core.exceptions import ValidationError
from summary.form import SummaryForm

class QAForm(SummaryForm):
    max_pages=10
    option_process=forms.ChoiceField(choices=(('none','Select An Option ----'),('page_process','Pages to Generate Questions and Answers'),('page_omit','Pages to Omit From Questions and Answers')),required=False)
    page_omit=forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={"placeholder":"Pages to omit From Questions and Answers"}))
    page_process=forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={"placeholder":"Pages to Generate Questions and Answers"}))