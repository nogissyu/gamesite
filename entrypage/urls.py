from django.urls import path

from . import views

urlpatterns = [
    path('entry/', views.entry_form, name='entry_form'),
    path('entrylist/', views.entry_list, name='entry_list'),
    path('deentry/', views.deentry_form, name='deentry_form'),
    path('redeentry/', views.redeentry_form, name='redeentry_form'),

]