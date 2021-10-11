from django.shortcuts import render
from django.views import View
from django.db import connection

# Create your views here.
class informe(View):
    template_name = 'informes/informe_global.html'
    def get(self, request, *args, **kwargs):
        cursor = connection.cursor()
        #cursor.execute("SELECT fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY institucion_id")
        #cursor.execute("SELECT strftime('%m',fecha) as fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY strftime('%m',fecha)")
        cursor.execute("SELECT strftime('%m',fecha) as fecha, SUM(cantidad_aceite) FROM aceite_registro_aceite GROUP BY strftime('%m',fecha)")
        resultado = cursor.fetchall()
        print(resultado)