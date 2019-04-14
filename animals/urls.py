from django.urls import path, re_path
from . import views

app_name = "animals"

urlpatterns = [
    re_path("^all/$", views.AnimalList.as_view(), name="all"),
    path("all/<int:animal_id>/", views.get_animal, name="get_animal"),
    path("dogs/", views.get_all_dogs, name="dogs"),
    path("all/ordered/", views.order_animals, name="ordered"),
    path("create/", views.create_animal_form, name="create"),
    re_path("^edit/(?P<pk>\d+)/$", views.AnimalUpdate.as_view(), name="edit"),
    path("delete/<int:animal_id>/", views.delete, name="delete"),
]
