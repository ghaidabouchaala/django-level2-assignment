from django import forms
from django.core import validators
from level_two_app.models import Users

# custom validation function
"""def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name has to start with z")
class FormName(forms.Form):
    name =forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter your email again')
    text = forms.CharField(widget = forms.Textarea)
   # botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,validators=[validators.MaxLengthValidator(0)]) 


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail =all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make email match")
"""  



class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'






