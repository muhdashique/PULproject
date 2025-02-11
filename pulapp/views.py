from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import FuelRate, GalleryImage
from .forms import FuelRateForm, GalleryImageForm






# Create your views here.
def index(request):
    fuel_rates = FuelRate.objects.all()
    gallery_images = GalleryImage.objects.all()[:6]
    
    context = {
        'fuel_rates': fuel_rates,
        'gallery_images': gallery_images,  
    }
    
    return render(request, 'index.html', context)


def about(request):
    return render(request,'about.html')


def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})



def contact(request):
    return render(request,'contact.html')




def adminpannel(request):
    fuel_rates = FuelRate.objects.all()
    
    if request.method == 'POST':
        form = FuelRateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminpannel')  
    else:
        form = FuelRateForm()
    
    context = {
        'fuel_rates': fuel_rates,
        'form': form,
    }
    return render(request, 'adminpannel.html', context)





def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('adminpannel') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')





def edit_fuel_rate(request, pk):
    fuel_rate = get_object_or_404(FuelRate, pk=pk)
    if request.method == 'POST':
        form = FuelRateForm(request.POST, instance=fuel_rate)
        if form.is_valid():
            form.save()
            return redirect('adminpannel')  
    else:
        form = FuelRateForm(instance=fuel_rate)
    return render(request, 'edit_fuel_rate.html', {'form': form})



def delete_fuel_rate(request, pk):
    fuel_rate = get_object_or_404(FuelRate, pk=pk)
    if request.method == 'POST':
        fuel_rate.delete()
        return redirect('adminpannel')  
    return render(request, 'confirm_delete.html', {'fuel_rate': fuel_rate})




def user_logout(request):
    logout(request)
    return redirect('index')  


def add_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_image')  # Redirect after successful submission
    else:
        form = GalleryImageForm()  # Ensure form is defined for GET request
    
    images = GalleryImage.objects.all()  # Fetch images to display
    return render(request, 'add_image.html', {'form': form, 'images': images})




def edit_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('add_image')  
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'edit_image.html', {'form': form, 'image': image})

def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        image.delete()
        return redirect('add_image') 
    return render(request, 'delete_image.html', {'image': image})
