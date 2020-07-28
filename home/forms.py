from django import forms
from .models import (Event,
    EventDetail)
from django.forms.models import BaseInlineFormSet, inlineformset_factory


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ("title","topic","start_date","end_date","Email")
        widgets= {
                'title': forms.TextInput(attrs={'class': 'form-control'}),    
                'topic': forms.TextInput(attrs={'class': 'form-control'}),
                'start_date': forms.DateInput(attrs={'class': 'form-control'}),
                'end_date': forms.DateInput(attrs={'class': 'form-control'}),
                'Email': forms.EmailInput(attrs={'class': 'form-control'}),
                }



class EventDetailForm(forms.ModelForm):
    
    class Meta:
        model = EventDetail
        fields = ("event","time","description")

EventDetailFormSet = inlineformset_factory(Event,EventDetail,extra=1,min_num=2,form = EventDetailForm, can_delete = True)
