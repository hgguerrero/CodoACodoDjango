from django import forms

class Alta_cliente_form(forms.Form):
    nombre = forms.CharField(label= "nombre y apellido", required=True)