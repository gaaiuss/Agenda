from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Type your first',
            },
        ),
        label='Name',
        help_text='Help text for user'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Type your first',
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Type your first name',
        #         }
        #     ),
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'First name cannot be equal to last name',
                code='invalid',
            )
            self.add_error('first_name', msg,)
            self.add_error('last_name', msg,)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Name cannot be "ABC"',
                    code='invalid'
                )
            )

        return first_name
