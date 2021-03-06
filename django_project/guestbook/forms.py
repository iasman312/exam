from django import forms


class SearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=False, label='Найти '
                                                                    'автора')