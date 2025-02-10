from django.urls import path
from . import views  # Ensure this import works correctly

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('adminpannel/', views.adminpannel, name='adminpannel'),
    path('login/', views.user_login, name='login'),
    path('edit/<int:rate_id>/', views.edit_fuel_rate, name='edit_fuel_rate'),
    path('delete/<int:rate_id>/', views.delete_fuel_rate, name='delete_fuel_rate'),
    path('edit_fuel_rate/<int:pk>/', views.edit_fuel_rate, name='edit_fuel_rate'),  
    path('delete_fuel_rate/<int:pk>/', views.delete_fuel_rate, name='delete_fuel_rate'),
    path('logout/', views.user_logout, name='logout'),
    path('add-image/', views.add_image, name='add_image'),
    path('edit-image/<int:image_id>/', views.edit_image, name='edit_image'),
    path('delete-image/<int:image_id>/', views.delete_image, name='delete_image'),
 

]