from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'NOM', 'PRENOM', 'POSTNOM', 'UNIVERSITE', 'PROGRAMME', 'FACULTE', 'DEPARTEMENT', 'LOGEMENT', 'NOM_DU_PERE', 'NOM_DE_LA_MERE', 'PHOTO', 'DIPLOMES', 'COPIE_DU_PASSPORT', 'NIVEAU_EN_ANGLAIS', 'PAYS', 'NUMERO_DE_TEL']
