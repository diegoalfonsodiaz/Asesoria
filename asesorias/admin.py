from django.contrib import admin



from .models import Proyecto, ProyectoAdmin, Asesor, AsesorAdmin



admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Asesor, AsesorAdmin)