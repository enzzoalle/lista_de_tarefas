from django import forms
from .models import Materia, Comentario

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['text']
        labels = {'text': ''}

class ComentarioForm(forms.ModelForm):
        class Meta:
            model = Comentario
            fields = ['text']
            labels = {'text': ''}
            widgets = {'text': forms.Textarea(attrs={'cols':50})}