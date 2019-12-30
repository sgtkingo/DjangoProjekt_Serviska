"""servis_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import records.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', records.views.home, name="home"),
    path('records/index', records.views.records_index, name="records_index"),
    path('records/<int:record_id>/', records.views.record_detail, name="record_detail"),
    path('persons/index', records.views.person_index, name="persons_index"),
    path('persons/<int:person_id>/', records.views.person_detail, name="person_detail"),
    path('materials/list', records.views.show_material_list, name="material_list"),
    path('materials/<int:material_id>/', records.views.show_material_detail, name="material_detail"),
    path('records/edit/<int:record_id>/', records.views.record_edit, name='record_edit'),
    path('records/add/', records.views.record_add, name='record_add'),
    path('persons/edit/<int:person_id>/', records.views.person_edit, name='person_edit'),
    path('materials/edit/<int:material_id>/', records.views.material_edit, name='material_edit'),
    path('records/<int:record_id>/edit_solution/', records.views.solution_edit, name='solution_edit'),
    path('records/<int:record_id>/new_solution/', records.views.solution_add, name='solution_add'),
    path('records/<int:record_id>/delete_solution/', records.views.solution_delete, name='solution_delete'),
]
