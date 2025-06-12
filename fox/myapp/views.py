from django.shortcuts import render, redirect
from .forms import LoginForm
from django.shortcuts import render

def homepage1(request):
    return render(request,'login.html')
def homepage2(request):
    return render(request,'list.html')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect('success')  
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def success_view(request):
    return render(request,'success.html')

