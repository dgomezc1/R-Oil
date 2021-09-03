"""Student views."""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def signup_view(request):
    """Sign up view."""
    return render(request, 'estudiante/signup.html')