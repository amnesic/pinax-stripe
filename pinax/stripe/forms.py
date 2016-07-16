from django import forms

from .models import Plan


class PlanForm(forms.Form):
    queryset = Plan.objects.exclude(statement_descriptor = "hidden")
    plan = forms.ModelChoiceField(queryset)
