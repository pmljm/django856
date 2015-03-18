from django import forms


class contactForm(forms.Form):
    ''' Making a signup, login, logout for for future users '''
    name = forms.CharField(required=False, max_length=100, help_text='100 characters max')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)