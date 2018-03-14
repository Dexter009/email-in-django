from django import forms

from myapp.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model=Question
        fields=['name','age','height']

    image=forms.FileField()