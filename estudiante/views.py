"""Student views."""

# Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Forms
from estudiante.forms import SignupForm, EstudianteForm

# Create your views here.
@login_required
def signup_view(request):
    """Sign up user view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
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
