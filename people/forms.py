from django import forms
from countries.models import Country
from people.models import Person

class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first name')
    last_name = forms.CharField(label='last name')
    nacionality = forms.ModelMultipleChoiceField(queryset=Country.objects.all())
    father = forms.ModelChoiceField(required=False, queryset=Person.objects.all())
    active = forms.BooleanField()
    email = forms.EmailField()
