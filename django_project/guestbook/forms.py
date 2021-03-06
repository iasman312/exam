from django import forms
from django.forms import widgets


class FeedbackForm(forms.Form):

    author = forms.CharField(max_length=150, required=True,
                             widget=forms.TextInput(attrs={'placeholder':
                                                               'Name'}),
                             label='Автор')
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email Address'}), label='Почта автора')
    text = forms.CharField(max_length=2000, required=True,
                           widget=widgets.Textarea, label='Текст записи')


class SearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=False, label='Найти '
                                                                    'автора')