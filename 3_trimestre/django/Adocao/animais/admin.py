from django.contrib import admin

# importar modelos

from .models import *

# Register your models here.

admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Animal)
