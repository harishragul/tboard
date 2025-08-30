from django import forms
from tasks.models import Task

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=200, required=True)
#     password = forms.CharField(widget=forms.PasswordInput())

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

    def __init__(self, *args, organization=None, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if organization is not None:
            # Filter assigned_to to only members of this organization
            self.fields['assigned_to'].queryset = self.fields['assigned_to'].queryset.filter(organization=organization)
            # Hide assigned_by field since it will be set automatically to the current user
            if 'assigned_by' in self.fields:
                self.fields['assigned_by'].widget = forms.HiddenInput()
                if user:
                    # Set the assigned_by to the current user's member record
                    from teams.models import Member
                    try:
                        member = Member.objects.get(user=user, organization=organization)
                        self.fields['assigned_by'].initial = member
                    except Member.DoesNotExist:
                        pass
            # Filter status to only statuses of this organization
            if 'status' in self.fields:
                self.fields['status'].queryset = self.fields['status'].queryset.filter(organization=organization)
            # Optionally, hide or set the organization field
            if 'organization' in self.fields:
                self.fields['organization'].initial = organization
                self.fields['organization'].queryset = self.fields['organization'].queryset.filter(id=organization.id)
                self.fields['organization'].disabled = True
        