from django.urls import path

from . import views


urlpatterns = [
    path('addbank', views.fn_add_bank),
    path('list', views.fn_get_list_of_banks),
]
