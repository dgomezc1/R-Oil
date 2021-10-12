# Django
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def informe(request):
    """Sign up user view."""
    
    return render(
        request=request, 
        template_name='informes/informe.html'
        
    )
