from django import forms
from .models import Patient, Symptom, Disease

class IdentityForm(forms.ModelForm):

    NIS = forms.CharField(

        widget = forms.TextInput(

                attrs = {

                        'placeholder': 'Enter NIS',
                                'class' : 'form-control'
                }
        )
    )

    first_name = forms.CharField(
            widget = forms.TextInput(

                    attrs = {

                            'placeholder': 'Enter First Name',
                            'class' : 'form-control'
                    }
            )
    )



    last_name = forms.CharField(
            widget = forms.TextInput(

                    attrs = {

                              'placeholder': 'Enter Last Name',
                             'class' : 'form-control'
                    }
            )
    )


    contact = forms.CharField(
        widget = forms.TextInput(

                attrs = {

                        'placeholder':'Enter Contact',
                                'class':'form-control'
                }
        )
    )

    born = forms.DateField(

            widget = forms.TextInput(
                    attrs = {

                        'placeholder' : 'Enter Birth',
                            'class':'form-control'

                    }
            )
    )

    location = forms.CharField(
        widget = forms.TextInput(

                attrs = {

                        'placeholder':'Enter location',
                                'class':'form-control'
                }
        )
    )

    email_address = forms.CharField(
            widget = forms.TextInput(

                    attrs = {

                            'placeholder':'Enter email address',
                                    'class':'form-control'
                    }
            )
        )

    class Meta:

        model = Patient
        fields = ['NIS', 'first_name', 'last_name', 'born', 'location', 'contact', 'email_address', ]



class SymptomForm(forms.ModelForm):

        identity = forms.CharField(
                widget = forms.TextInput(
                        attrs = {

                                'placeholder': 'Name of Symptom',
                                'class' : 'form-control'
                        }
                )
        )

        description= forms.CharField(
            widget=forms.Textarea(
                    attrs = {

                            'placeholder':'Explain Medical condition',
                            'class':'form-control'
                    }
            )
    )
        class Meta:

            model = Symptom
            fields = ['identity', 'description']

class DiseaseForm(forms.ModelForm):

    identity = forms.CharField(
            widget = forms.TextInput(
                    attrs = {

                            'placeholder': 'Name of Disease',
                            'class' : 'form-control'
                    }
            )
    )

    description= forms.CharField(
        widget=forms.Textarea(
                attrs = {
                        'placeholder':'Explain Medical condition',
                        'class':'form-control'
                }
        )
)
    class Meta:

        model = Disease
        fields = ['identity', 'description']
