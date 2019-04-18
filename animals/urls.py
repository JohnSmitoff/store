from django.urls import path, re_path
from . import views

app_name = "animals"
# app_name = 'owners'

urlpatterns = [
    re_path("^all/$", views.AnimalList.as_view(), name="all"),
    path("all/<int:animal_id>/", views.get_animal, name="get_animal"),
    path("dogs/", views.get_all_dogs, name="dogs"),
    path("all/ordered/", views.order_animals, name="ordered"),
    path("create/", views.AnimalCreate.as_view(), name="create"),
    re_path("^edit/(?P<pk>\d+)/$", views.AnimalUpdate.as_view(), name="edit"),
    re_path("^delete/(?P<pk>\d+)/$", views.AnimalDelete.as_view(), name="delete"),
    path("owners/", views.OwnerList.as_view(), name="owners"),
    path("owner/create/", views.CreateOwner.as_view(), name="create_owner"),
    re_path("^owner/delete/(?P<pk>\d+)/$", views.DeleteOwner.as_view(), name="delete_owner"),
    re_path('details/(?P<pk>[-\w]+)/', views.AnimalDetail.as_view(), name='details'),
]
