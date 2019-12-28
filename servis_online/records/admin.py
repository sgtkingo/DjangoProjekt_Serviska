from django.contrib import admin

# Register your models here.

from records.models import Record,Person,Solution,Material
admin.site.register(Record)
admin.site.register(Person)
admin.site.register(Solution)
admin.site.register(Material)