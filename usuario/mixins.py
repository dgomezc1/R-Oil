from django.shortcuts import redirect

class permisos_institucion_docentes(object):
    def pertenece(usuario):
        if usuario.groups.filter(name__in =['admin']) or usuario.is_superuser:
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if permisos_institucion_docentes.pertenece(request.user):
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')