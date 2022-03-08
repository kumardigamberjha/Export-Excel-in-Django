from django import forms

from .models import SalaryModel
from .admin import SalaryAdmin

class SalaryForms(forms.ModelForm):
    class Meta:
        model = SalaryModel
        fields = "__all__"