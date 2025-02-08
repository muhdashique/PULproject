from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import FuelRate
from .forms import FuelRateForm
from .models import FuelRate  # Change this to FuelRate (singular)




# Create your views here.

def index(request):
    fuel_rates = FuelRate.objects.all()
    context = {
        'fuel_rates': fuel_rates,
    }
    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')



def gallery(request):
    return render(request,'gallery.html')




def contact(request):
    return render(request,'contact.html')




def adminpannel(request):
    fuel_rates = FuelRate.objects.all()
    
    if request.method == 'POST':
        form = FuelRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpannel')  # Redirect to avoid duplicate form submission
    else:
        form = FuelRateForm()
    
    context = {
        'fuel_rates': fuel_rates,
        'form': form,
    }
    return render(request, 'adminpannel.html', context)




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpannel')  # Redirect to home or a page of your choice
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



from django.shortcuts import render, get_object_or_404, redirect
from .models import FuelRate
from .forms import FuelRateForm

def edit_fuel_rate(request, pk):
    fuel_rate = get_object_or_404(FuelRate, pk=pk)
    if request.method == 'POST':
        form = FuelRateForm(request.POST, instance=fuel_rate)
        if form.is_valid():
            form.save()
            return redirect('adminpannel')  # Redirect to the list view after saving
    else:
        form = FuelRateForm(instance=fuel_rate)
    return render(request, 'edit_fuel_rate.html', {'form': form})


from django.shortcuts import get_object_or_404, redirect
from .models import FuelRate

def delete_fuel_rate(request, pk):
    fuel_rate = get_object_or_404(FuelRate, pk=pk)
    if request.method == 'POST':
        fuel_rate.delete()
        return redirect('adminpannel')  # Redirect to the list of fuel rates after deletion
    return render(request, 'confirm_delete.html', {'fuel_rate': fuel_rate})


from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('index')  # Redirect to the login page after logout
