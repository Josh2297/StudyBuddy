from django import forms
import pdfplumber
import re
from django.core.exceptions import ValidationError


class SummaryForm(forms.Form):
    book_title = forms.CharField(
        max_length=100,
        help_text="Name of Book (Optional)",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter Text Title"}))
    book_path = forms.FileField(required=True, max_length=500)
    option_process = forms.ChoiceField(
        choices=(
            ('none',
             'Select An Option ----'),
            ('page_process',
             'Enter Pages to Summarize'),
            ('page_omit',
             'Enter Pages to Omit From Summary')),
        required=False)
    page_omit = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pages to omit From Summary"}))
    page_process = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pages to Summarize"}))
    summary_path = forms.FileField(required=False, max_length=100)

    class Meta:
        exclude = ('summary_path', 'page_omit', 'page_process')

    max_pages = 10

    def clean_book_path(self):
        value = self.cleaned_data.get('book_path')
        with pdfplumber.open(value) as pdf:
            num_of_pages = len(pdf.pages)
            self.num_of_pages = num_of_pages
        '''
        if num_of_pages>75:
            raise ValidationError('Book too large for Processing.Upload a book less than 75 pages or use the select pages to extract/exculde features')
        else:
            return value'''
        if value.size > 100000000:
            raise ValidationError(
                "File Size " + str(int(value.size) / 1000000) + "MB too large for processing.")
        if value.name.endswith("pdf"):
            return value
        else:
            raise ValidationError("Please Upload a Document (.pdf)")

    def clean_page_process(self):
        value = self.cleaned_data.get('page_process')
        if value:
            value = re.split(r'[^(0-9|\-)]', value)
            main_val = []
            for x in value:
                if re.search(r'\-', x):
                    range_ind = re.split(r'\-', x)
                    if len(range_ind) == 2:
                        try:
                            range_ind = [int(x) for x in range(
                                int(range_ind[0]), int(range_ind[1]) + 1)]
                        except ValueError:
                            raise ValidationError('Please Enter Valid Number')

                    else:
                        raise ValidationError(
                            "Range of Index to Exclude Greater Than 2 Note range should be '1-5'")

                    main_val.extend(range_ind)
                else:
                    try:
                        main_val.append(int(x))
                    except ValueError:
                        raise ValidationError('Enter Valid Number')
            main_val.sort()
            if main_val[0] == 0:
                main_val = main_val[1:]
            if max(main_val) > self.num_of_pages:
                raise ValidationError(
                    "Invalid Page Number Entered. Maximum  Number of Pages in Text is " + str(self.num_of_pages))
            if len(set(main_val)) > self.max_pages:
                raise ValidationError(
                    'Pages specified above 10, Reduce the Number of Pages to Summarize')
            else:
                return list(set(main_val))
        else:
            return value

    def clean_page_omit(self):
        value = self.cleaned_data.get('page_omit')
        if value:
            value = re.split(r'[^(0-9|\-)]', value)
            main_val = []
            for x in value:
                if re.search(r'\-', x):
                    range_ind = re.split(r'\-', x)
                    if len(range_ind) == 2:
                        try:
                            range_ind = [int(x) for x in range(
                                int(range_ind[0]), int(range_ind[1]) + 1)]
                        except ValueError:
                            raise ValidationError('Please Enter Valid Number')

                    else:
                        raise ValidationError(
                            "Range of Index to Exclude Greater Than 2 Note range should be '1-5'")

                    main_val.extend(range_ind)
                else:
                    try:
                        main_val.append(int(x))
                    except ValueError:
                        raise ValidationError('Enter Valid Number')
            num_of_pages = [x for x in range(1, self.num_of_pages)]
            main_val.sort()
            if main_val[0] == 0:
                main_val = main_val[1:]
            main_val = set(num_of_pages) - set(main_val)
            if len(set(main_val)) > self.max_pages:
                raise ValidationError(
                    'Pages specified above 10, Reduce the Number of Pages to Summarize')
            elif len(main_val) < 1:
                raise ValidationError(
                    'Invalid Book Page Range Entered: Specify Pages in the Book range')
            else:
                return list(set(main_val))
        else:
            return value

    def clean(self):
        value = super(SummaryForm, self).clean()
        if value.get('page_process') or value.get('page_omit'):
            pass
        else:
            if self.num_of_pages > self.max_pages:
                self.add_error(
                    'book_path',
                    'Number of Pages Greater Than 10. Specify pages to summarize or exclude')
