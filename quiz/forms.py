from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'student_id', 'phone_num']
        widgets = {
            'name': forms.TextInput(attrs={
                'class' : 'input__name',
                'id' : 'id_name',
                'placeholder' : '이름을 작성해주세요.'
                }),
            'student_id': forms.TextInput(attrs={
                'class': 'input__student_id',
                'id': 'id_student_id',
                'placeholder' : '학번을 작성해 주세요. (ex.2171234)'
                }),
            'phone_num': forms.TextInput(attrs={
                'class': 'input__phone_num',
                'id': 'id_phone_num',
                'placeholder' : '전화번호를 작성해 주세요. (ex.01000000000)'
                }),
        }
