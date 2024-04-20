from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data (create user, etc.)
            # Redirect to a success page or perform any other action
            return redirect('success_url')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
