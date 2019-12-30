from django import forms
from records.models import Record, Person, Solution, Material

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        #fields = ['cars_capacity', 'name', 'company']
        exclude = []

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        exclude = []

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        exclude = []
