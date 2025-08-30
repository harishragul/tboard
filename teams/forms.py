from django import forms
from teams.models import Organization

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=200, required=True)
#     password = forms.CharField(widget=forms.PasswordInput())

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
        