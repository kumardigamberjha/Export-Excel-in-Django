from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save_excel_data/", views.ExportFile, name="export-file")
]