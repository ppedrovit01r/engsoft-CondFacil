from django.contrib import admin
from login.models import Condominio, Pessoa, Relatorio

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Condominio)
admin.site.register(Relatorio)