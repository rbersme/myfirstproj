from django.contrib import admin

from mrmala.contato.models import Cadastro

class CadastroAdmin(admin.ModelAdmin):
    model=Cadastro
    list_display = ['codigo', 'nome', 'telefone1', 'email']
    list_filter = ['nome', 'sexo', 'est_civil']
    search_fields = ['nome']
    save_on_top = True
admin.site.register(Cadastro, CadastroAdmin) 

# Register your models here.
