from django.contrib import admin

# Register your models here.
from .models import Post,UNIVERSITE,PROGRAMME,NATIONALITE,faculté,CAMPUS,Departement

admin.site.register(Post)
admin.site.register(UNIVERSITE)
admin.site.register(PROGRAMME)
admin.site.register(NATIONALITE)
admin.site.register(faculté)
admin.site.register(Departement)
admin.site.register(CAMPUS)