from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    v_email = forms.EmailField(label='Enter your email field again: ')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        entire_form_data = super().clean()
        email = entire_form_data['email']
        verifymail = entire_form_data['v_email']

        if email != verifymail:
            raise forms.ValidationError('Email fields do not match')

        # if all_clean_data['email'] != all_clean_data['verify_email']:
        #     raise forms.ValidationError('Email fields do not match')
