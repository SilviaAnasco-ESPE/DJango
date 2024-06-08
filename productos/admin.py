from django.contrib import admin
from .models import Categoria, Producto
from import_export.admin import ImportExportModelAdmin

admin.site.register(Categoria, ImportExportModelAdmin)
admin.site.register(Producto, ImportExportModelAdmin)
