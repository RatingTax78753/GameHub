from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(Feedback)
admin.site.register(Topico)
admin.site.register(ConteudoTopico)
