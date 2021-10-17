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

class permisos_estudiante_aceite(object):
    def pertenece(usuario):
        if usuario.groups.filter(name__in =['admin']) or usuario.is_superuser or usuario.groups.filter(name__in =['docentes']):
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if permisos_estudiante_aceite.pertenece(request.user):
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')

class permisos_registro_admin(object):
    def pertenece(usuario):
        if usuario.is_staff or usuario.is_superuser:
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):
        if permisos_registro_admin.pertenece(request.user):
            return super().dispatch(request, *args, **kwargs)
        return redirect('home')