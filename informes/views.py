# Django
import django
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db import connection
from instituciones.models import Institucion
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Models
from docente.models import Docente
from usuario.models import User
from aceite.models import registro_aceite

# Create your views here.
class informeGlobal(View):
    template_name = 'informes/informe_global.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_data(valor):
        cursor = connection.cursor()
        if valor == "colum":
            cursor.execute("SELECT strftime('%m',fecha) as fecha, institucion_id, SUM(cantidad_aceite) FROM aceite_registro_aceite GROUP BY institucion_id,strftime('%m',fecha) ORDER BY institucion_id")
        elif valor == "pie":
            cursor.execute("SELECT E.grado, SUM(A.cantidad_aceite) FROM estudiante_estudiante E JOIN aceite_registro_aceite A ON E.id = A.estudiante_id GROUP BY E.grado")
        resultado = cursor.fetchall()
        return resultado

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'get_colum':   
                data = conversion_colum(informeGlobal.get_data("colum"))
            elif action == 'get_pie':
                data ={
                    'name': 'Porcentaje Aceite',
                    'colorByPoint': True,
                    'data':conversion_pie(informeGlobal.get_data("pie")),
                } 
            else:
                data['error']="Ha ocurrido un error"
        except Exception as e:
            data['error']  = str(e)

    def get(self, request, *args, **kwargs): 
        #cursor.execute("SELECT fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY institucion_id")
        #cursor.execute("SELECT strftime('%m',fecha) as fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY strftime('%m',fecha)")
        return render(request, 'informes/informe_global.html')

class informeLocal(View):
    template_name = 'informes/informe_local.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institucion'] = Institucion.objects.get(pk=2)
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_data(valor):
        cursor = connection.cursor()
        if valor == "colum":
            cursor.execute("SELECT strftime('%Y %m',fecha) as fecha, institucion_id, SUM(cantidad_aceite) FROM aceite_registro_aceite WHERE institucion_id=2 GROUP BY institucion_id,strftime('%m',fecha) ORDER BY institucion_id ")
        elif valor == "pie":
            cursor.execute("SELECT E.grado, SUM(A.cantidad_aceite) FROM estudiante_estudiante E JOIN aceite_registro_aceite A ON E.id = A.estudiante_id WHERE institucion_id=2 GROUP BY E.grado")
        resultado = cursor.fetchall()
        return resultado

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            #docente = User.objects.get(username = request.user)
            #institucion  =  (Docente.objects.get(user = docente)).institucion
            #resultado = registro_aceite.objects.filter(institucion_id = 2)
            if action == 'get_colum':
                data = conversion_colum(informeGlobal.get_data("colum"))
            elif action == 'get_pie':
                data ={
                    'name': 'Porcentaje Aceite',
                    'colorByPoint': True,
                    'data':conversion_pie(informeGlobal.get_data("pie")),
                } 
            else:
                data['error']="Ha ocurrido un error"
        except Exception as e:
            data['error']  = str(e)
        return JsonResponse(data, safe = False)


    def get(self, request, *args, **kwargs): 
        #cursor.execute("SELECT fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY institucion_id")
        #cursor.execute("SELECT strftime('%m',fecha) as fecha, cantidad_aceite, institucion_id FROM aceite_registro_aceite ORDER BY strftime('%m',fecha)")
        return render(request, 'informes/informe_local.html')

#def conversion(resultado):
def conversion_pie(resultado):
    total = 0
    for i in resultado:
        total = total+i[1]
    lista = []
    for i in resultado:
        porcentaje = (i[1]*100)/total
        diccionario = {'name':i[0]+'°', 'y': porcentaje}
        lista.append(diccionario)
    return lista

def conversion_colum(resultado):
    temp = (resultado[0])[1]
    lista = []
    lista_datos = []
    nombre = Institucion.objects.get(pk=(resultado[0])[1])
    diccionario = {'name':nombre.nombre}
    for i in range(len(resultado)):
        if (resultado[i])[1] == temp:
            lista_datos.append((resultado[i])[2])
        else:
            diccionario['data'] = lista_datos
            lista.append(diccionario)
            lista_datos =[]
            diccionario={}
            nombre = Institucion.objects.get(pk=(resultado[i])[1])
            diccionario['name']=nombre.nombre
            temp = (resultado[i])[1]
    diccionario['data'] = lista_datos
    lista.append(diccionario)
    return lista

