from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from records.models import Record,Person,Solution,Material

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def home(request):
    return render(request,"index.html")

def record_detail(request, record_id):
    record = get_object_or_404(Record,id=record_id)
    return render(request, "r_detail.html", {"t_record": record})

def records_index(request):
    records = Record.objects.all().order_by("id")
    return render(request,"r_index.html",{"t_records": records})

def person_detail(request, person_id):
    person = get_object_or_404(Person,id=person_id)
    records_bounds = Record.objects.all().filter(person_info=person)
    return render(request, "p_detail.html", {"t_person": person, "t_records_bounds": records_bounds})

def person_index(request):
    persons = Person.objects.all().order_by("id")
    return render(request,"p_index.html",{"t_persons": persons})

def show_material_list(request):
    materials = Material.objects.all().order_by("id")
    return render(request,"m_list.html",{"t_materials": materials})

def show_material_detail(request, material_id):
    material = get_object_or_404(Material,id=material_id)
    return render(request, "m_detail.html", {"t_material": material})