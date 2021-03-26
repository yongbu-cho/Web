from django import forms
from forum.models import Presenting, Suggestion


class PresentingForm(forms.ModelForm):
    class Meta:
        model = Presenting
        fields = ['subject', 'content']

        labels = {
            'subject': '제시 단어',
            'content': '단어 설명',
        }        

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['content']
        labels = {
            'content': '제안내용',
        }        