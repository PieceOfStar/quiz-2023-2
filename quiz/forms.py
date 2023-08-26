from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'student_id', 'phone_num']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input__name'}),
            'student_id': forms.TextInput(attrs={'class': 'input__student_id'}),
            'phone_num': forms.TextInput(attrs={'class': 'input__phone_num'}),
        }
