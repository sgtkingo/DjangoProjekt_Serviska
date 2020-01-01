from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from records.models import Record,Person,Solution,Material
from records.forms import RecordForm,PersonForm,MaterialForm,SolutionForm

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def home(request):
    return render(request,"index.html")

def stats(request):
    records = Record.objects.all().order_by("id")
    total_balance=0
    for record in records:
        total_balance=total_balance+record.getSolutionBalance()
    return render(request,"stats.html",{"t_records": records, "t_balance":total_balance})

def record_detail(request, record_id):
    record = get_object_or_404(Record,id=record_id)
    if request.method == 'POST':
        record.Resolve()
        record.save()
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

def record_edit(request, record_id):
    record = get_object_or_404(Record,id=record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance = record)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm(instance = record)
    return render(request, 'r_edit.html', {'form':form, 't_record':record})

def person_edit(request, person_id):
    person = get_object_or_404(Person,id=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance = person)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm(instance = person)
    return render(request, 'p_edit.html', {'form':form, 't_person':person})

def material_edit(request, material_id):
    material = get_object_or_404(Material,id=material_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance = material)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm(instance = material)
    return render(request, 'm_edit.html', {'form':form, 't_material':material})

def solution_edit(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    solution_obj = get_object_or_404(Solution,id=record.servis_solution.id)
    if request.method == 'POST':
        form = SolutionForm(request.POST, instance = solution_obj)
        if form.is_valid():
            form.save()
    else:
        form = SolutionForm(instance = solution_obj)
    return render(request, 's_edit.html', {'form':form,'t_record':record})

def solution_add(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    solution_new=None
    if request.method == 'POST':
        solution_new = Solution()
        form = SolutionForm(request.POST, instance = solution_new)
        if form.is_valid():
            form.save()
            solution_new.save()
            record.servis_solution=solution_new
            record.save()
            return record_detail(request, record.id)
    else:
        form = SolutionForm()
    return render(request, 's_add.html', {'form':form, 't_record':record})

def solution_delete(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    solution = get_object_or_404(Solution, id=record.servis_solution.id)
    records_bounds = Record.objects.all().filter(servis_solution=solution)
    if request.method == 'POST':
        record.servis_solution=None
        solution.delete()
        record.save()
        return record_detail(request,record.id)
    else:
        return render(request, 's_delete.html', {'t_solution':solution,'t_record':record,"t_records_bounds": records_bounds})

def record_add(request):
    record_new=None
    if request.method == 'POST':
        record_new = Record()
        form = RecordForm(request.POST, instance = record_new)
        if form.is_valid():
            record_new.save()
            form.save()
            return records_index(request)
    else:
        form = RecordForm()
    return render(request, 'r_add.html', {'form':form })

def person_add(request):
    person_new=None
    if request.method == 'POST':
        person_new = Person()
        form = PersonForm(request.POST, instance = person_new)
        if form.is_valid():
            person_new.save()
            form.save()
            return person_index(request)
    else:
        form = PersonForm()
    return render(request, 'p_add.html', {'form':form })

def material_add(request):
    material_new=None
    if request.method == 'POST':
        material_new = Material()
        form = MaterialForm(request.POST, instance = material_new)
        if form.is_valid():
            material_new.save()
            form.save()
            return show_material_list(request)
    else:
        form = MaterialForm()
    return render(request, 'm_add.html', {'form':form })

def record_delete(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'POST':
        record.delete()
        return records_index(request)
    else:
        return record_detail(request,record.id)

def person_delete(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        person.delete()
        return person_index(request)
    else:
        return person_detail(request,person.id)

def material_delete(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        material.delete()
        return show_material_list(request)
    else:
        return show_material_detail(request,material.id)