from django import forms

class TextInputForm(forms.Form):
    input_text = forms.CharField(label='Enter text', widget=forms.Textarea)