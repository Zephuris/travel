from typing import Any
from django import forms
from datetime import date
from .models import Travel
from django.contrib.auth.models import User
class TravelAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user', None)
        super(TravelAddForm,self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['min'] = str(date.today())
        self.fields['end_date'].widget.attrs['min'] = str(date.today())
    start_date = forms.DateField(widget = forms.DateInput(attrs={'type':'date',
                                                                 'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}))
    end_date = forms.DateField(widget = forms.DateInput(attrs={'type':'date',
                                                               'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}))
    tour_lead = forms.ModelChoiceField(queryset=Travel.objects.all(),required=False)
    class Meta:
        model = Travel
        fields = ['id','title','start_date','end_date','destination','description','tour_lead']
        widgets = {
                    'title':forms.TextInput(attrs={'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}),
                    'destination':forms.TextInput(attrs={'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300'}),
                    'description':forms.Textarea(attrs={'class':'mt-1 p-3 w-1/6 border rounded-md bg-gray-200 focus:outline-none focus:ring focus:border-blue-300',
                                                        'rows':4}),                          
                }
    def save(self, commit: bool = ...) -> Any:
        travel = Travel.objects.create(title = self.cleaned_data['title'],
                                       start_date = self.cleaned_data['start_date'],
                                       end_date = self.cleaned_data['end_date'],
                                       destination = self.cleaned_data['destination'],
                                       description = self.cleaned_data['description'],
                                       tour_lead = self._user)
        return travel

