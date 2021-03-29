from django import forms
from forum.models import Presenting


class PresentingForm(forms.ModelForm):
    class Meta:
        model = Presenting
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',    
        }