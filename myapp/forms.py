from django import forms

from myapp.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model=Question
        fields=['name','age','height']
        help_texts = {
            'name': 'Please enter your full name',
            'age': 'Please enter your full age',
            'height': 'Eg "5 ft 8 in"',

        }

    image=forms.FileField()