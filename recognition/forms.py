from django import forms

class Formulario(forms.Form):
    foto = forms.ImageField()
