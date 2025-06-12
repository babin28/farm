from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import render

# remove this below unused function
def homepage1(request):
    return render(request, 'login.html')

def homepage2(request):
    # rename this function and its template to index
    # create this function to get the list of fishes from FishModel
    """Index page -> shows availabe products."""
    return render(request, 'list.html')

def login_view(request):
    """Login view to check loggedin users"""

    if request.method == 'POST':
        form = LoginForm(request.POST)
    
        if form.is_valid():
            form.save()  # Save to database
            return redirect('success')  
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def success_view(request):
    """Success page after login"""
    return render(request,'success.html')

