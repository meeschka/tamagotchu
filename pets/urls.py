from django.urls import path
from . import views
urlpatterns= [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name='index'),
    path('pets/<int:pet_id>', views.pet_details, name='details'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete', views.PetDelete.as_view(), name='pets_delete'),
    path('pets/<int:pet_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('pets/<int:pet_id>/add_toy/<int:toy_id>', views.add_toy, name='add_toy'),
    path('pets/<int:pet_id>/remove_toy/<int:toy_id>', views.remove_toy, name='remove_toy'),
    path('pets/<int:pet_id>/add_photo', views.add_pet_photo, name='add_pet_photo'),
    path('toys/', views.ToyList.as_view(), name='toy_list'),
    path('toys/<int:pk>', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name='toy_delete'),
    path('toys/<int:toy_id>/add_photo', views.add_toy_photo, name='add_toy_photo'),
    path('accounts/signup', views.signup, name='signup'),
]