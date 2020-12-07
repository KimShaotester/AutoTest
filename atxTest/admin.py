from django.contrib import admin

# Register your models here.

from atxTest.models import Device, Case, Suite, Parameters
from django.contrib import admin

class ParametersAdmin(admin.TabularInline):
    list_display = ["key", "value"]
    model = Parameters
    extra = 1

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "ip", "mac"]

class CaseAdmin(admin.ModelAdmin):
    list_display = ["caseid", "casename", "casescripts", "casefr"]
    inlines = [ParametersAdmin]

class SuiteAdmin(admin.ModelAdmin):
    list_display = ["suiteid", "suitename", "suiteowner", "suitecase"]

# class JobAdmin(admin.ModelAdmin):
#     list_display = ["suite", "device", "jobowner", "suitecase"]

# admin.site.register([Device, Case, Suite])
admin.site.register(Device,DeviceAdmin)
admin.site.register(Case,CaseAdmin)
admin.site.register(Suite,SuiteAdmin)