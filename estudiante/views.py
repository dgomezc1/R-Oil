"""Student views."""

# Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required



# Forms
from estudiante.forms import SignupForm, EstudianteForm
from instituciones.models import Institucion
from docente.models import Docente

# Create your views here.
@login_required
def signup_view(request):
    """Sign up user view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            docente = list(Docente.objects.filter(user=request.user))
            institucion = docente[0].institucion
            form.save(institucion)
            return redirect('student_signup') 
    else: 
        form = SignupForm()

    return render(
        request=request, 
        template_name='estudiante/signup.html',
        context={
            'form': form
        }
    )
