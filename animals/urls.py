from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path("^all/$", views.get_all_animals, name="all"),
    path("all/<int:animal_id>/", views.get_animal, name="get_animal"),
    path("dogs/", views.get_all_dogs, name="dogs"),
    path("all/ordered/", views.order_animals, name="ordered"),
    path("create/", views.create_animal_form, name="create"),
    path("edit/<int:animal_id>/", views.edit_animal, name="edit"),
    path("delete/<int:animal_id>/", views.delete, name="delete"),

]
