from django import forms
from before.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"