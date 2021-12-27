from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        # fields user has to fill
        model = Question
        fields = ['question', 'wiki_terms']