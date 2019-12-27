from django.contrib import admin

# Register your models here.

from records.models import Record,Person,Solution
admin.site.register(Record)
admin.site.register(Person)
admin.site.register(Solution)
