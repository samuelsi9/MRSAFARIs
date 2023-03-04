
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
  
class  UNIVERSITE(models.Model):
    UNIVERSITENOM= models.CharField(max_length=100)
    def __str__(self) :
      return self.UNIVERSITENOM
class  PROGRAMME(models.Model):
    PROGRAMMENOM= models.CharField(max_length=100)
    def __str__(self) :
      return self.PROGRAMMENOM
class  NATIONALITE(models.Model):
    NATIONNOM= models.CharField(max_length=100)       
    def __str__(self) :
      return self.NATIONNOM
class faculté(models.Model):
    faculténom= models.CharField(max_length=100)
    def __str__(self) :
      return self.faculténom

    
class Departement(models.Model):
    Departement=models.ForeignKey(faculté,on_delete=models.SET_NULL, blank=True, null=True)
    Departementname= models.CharField(max_length=100)  
    def __str__(self) :
      return self.Departementname
    
class CAMPUS(models.Model):
    campus= models.CharField(max_length=100)  
    
    def __str__(self) :
      return self.campus

class Post(models.Model):  
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    NOM = models.CharField(max_length=50, default='') 
    PRENOM = models.CharField(max_length=50, default='') 
    POSTNOM=models.CharField(max_length=40,default='')
    UNIVERSITE= models.ForeignKey( UNIVERSITE, on_delete=models.SET_NULL, blank=True, null=True)
    PROGRAMME=models.ForeignKey(PROGRAMME,on_delete=models.SET_NULL, blank=True, null=True)
    FACULTE = models.ForeignKey(faculté, on_delete=models.SET_NULL, blank=True, null=True)
    DEPARTEMENT = models.ForeignKey(Departement, on_delete=models.SET_NULL, blank=True, null=True)
    LOGEMENT=models.ForeignKey(CAMPUS,on_delete=models.SET_NULL, blank=True, null=True)  
    NOM_DU_PERE = models.CharField(max_length=50, default='') 
    NOM_DE_LA_MERE = models.CharField(max_length=50, default='')
    PHOTO = models.ImageField(default=' ', upload_to='PHOTO_pics')
    DIPLOMES =models.FileField(default=' ', upload_to='DIPLOME/')
    COPIE_DU_PASSPORT=models.FileField(default=' ', upload_to='passport/')
    NIVEAU_EN_ANGLAIS=models.FileField(default=' ', upload_to='NIVEAU/')
    PAYS =models.ForeignKey(NATIONALITE,on_delete=models.SET_NULL, blank=True, null=True)
    NUMERO_DE_TEL = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self) :
        return self.NOM
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
   
