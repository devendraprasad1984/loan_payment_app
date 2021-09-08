from django.urls import path

from . import views


urlpatterns = [
    path('loan', views.fn_loan),
    path('payment', views.fn_payment),
    path('balance', views.fn_balance),
]
