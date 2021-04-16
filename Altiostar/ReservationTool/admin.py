from django.contrib import admin
from ReservationTool.models import Device
from ReservationTool.models import Setup
from import_export.admin import ImportExportModelAdmin

class DeviceAdmin(ImportExportModelAdmin):
     pass

admin.site.register(Device, DeviceAdmin)
admin.site.register(Setup)

