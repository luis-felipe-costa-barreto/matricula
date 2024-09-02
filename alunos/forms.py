from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = '__all__'