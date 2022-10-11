from django.shortcuts import redirect, render  
from django.contrib.auth.forms import UserCreationForm  
from .forms import UserForm
# Create your views here.  
  
def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login')
    else:
        form = UserForm()


    return render(request, 'users/sign_up.html', {'form': form}) 

def profile(request):
    return render(request,'users/profile.html')