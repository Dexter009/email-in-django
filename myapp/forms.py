from django import forms


class QuestionForm(forms.Form):
    name=forms.CharField()
    age=forms.CharField()
    height=forms.CharField()
    image=forms.FileField()