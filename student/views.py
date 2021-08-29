"Student views."

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def signup_view(request):
    """Sign up view"""
    return render(request, 'student/signup.html')