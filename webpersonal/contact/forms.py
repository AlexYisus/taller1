from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu nombre'}),min_length=3, max_length=100)
    email=forms.EmailField(label="Email", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu email'}))
    subject=forms.CharField(label="Asunto",required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu asunto'}),min_length=5, max_length=100)
    message=forms.CharField(label="Mensaje", required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe un mensaje'}),min_length=5,max_length=1000)