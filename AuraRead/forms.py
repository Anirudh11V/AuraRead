from django import forms
from django.forms import ModelForm

from . models import PdfDocumnet


class PdfUploadForm(ModelForm):
    class Meta:
        model = PdfDocumnet
        fields = ['File']


class PageRangeForm(forms.Form):
    pdf_id = forms.IntegerField(widget= forms.HiddenInput())

    # Input for the starting page number
    start_page = forms.IntegerField(
        label= 'Start Reading from Page',
        min_value= 1,
        initial= 1,
        help_text= 'Enter the page number to start reading (e.g., 5)'
    )

    # Input for the ending page number
    end_page = forms.IntegerField(
        label= 'Stop Reading at page',
        min_value= 1,
        help_text= 'Enter the page number to stop reading (e.g., 8)'
    )
    