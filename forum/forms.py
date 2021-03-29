from django import forms
from forum.models import Presenting, Suggestion


class PresentingForm(forms.ModelForm):
    class Meta:
        model = Presenting
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',    
        }


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['content']
        labels = {
            'content': '답변내용',
        }        