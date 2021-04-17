from django.shortcuts import render, HttpResponse
from ReservationTool.models import Device
from .models import Device,Setup
from django.views.generic.base import TemplateResponseMixin, View
import csv,random,string
from .filters import SetupFilter
from .filters import DeviceFilter


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def add_device(request):
    if request.method == "POST":
        hostname = request.POST.get('hostname')
        ip = request.POST.get('ip')
        serial_number = request.POST.get('serial_number')
        mac = request.POST.get('mac')
        device_type = request.POST.get('device')
        make = request.POST.get('make')
        slug = rand_slug()
        new_slug = slug + '-' +hostname.lower()
        device = Device(hostname=hostname ,slug=new_slug, ip=ip , serial_number=serial_number , mac=mac , device_type=device_type , make=make)
        device.save()
    return render(request, "add_device.html", {})

def view_device(request):
    context = {}
    entries = Device.objects.all()
    context['entries'] = entries
    return render(request, 'view_device.html', context)


class AddSetupView(TemplateResponseMixin, View):
    template_name = 'add_setup.html'

    def dispatch(self, request):
        return super(AddSetupView, self).dispatch(request)

    def get(self, request, *args, **kwargs):
        devices = Device.objects.filter(setup__isnull=True)

        type = ["Select Device Type","CU","DU","RRH","UE","STU","UE Laptop","EPC","5G Core","Programmable Attenuators"]
        return self.render_to_response({'devices':devices,"type":type})

    def post(self, request, *args, **kwargs):
        devices = Device.objects.filter(setup__isnull=True)
        type = ["Select Device Type","CU","DU","RRH","UE","STU","UE Laptop","EPC","5G Core","Programmable Attenuators"]
        dict = request.POST.copy()
        print(dict)
        print(len(dict))
        csrf = dict.pop('csrfmiddlewaretoken')
        setup_name = dict.pop('setup_name')[0]
        setup_type = dict.pop('setup_type')[0]
        for key, value in dict.items():
            object = Device.objects.get(slug=value)
            try:
               Setup.objects.get(device_type=object)
            except:
               setup=Setup(setup_name=setup_name,device_type=object, setup_type=setup_type)
               setup.save()
        return self.render_to_response({'devices':devices,"type":type})


def view_setup(request):
    context = {}
    setup_entries = Setup.objects.all()
    context['setup_entries'] = setup_entries
    return render(request, 'view_setup.html', context)

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fields.csv"'


    writer = csv.writer(response)
    writer.writerow(['Hostname', 'IP', 'MAC', 'Device Type', 'Serial Number', 'Make/Model'])

    for fields in Device.objects.all().values_list('hostname', 'ip', 'mac', 'device_type','serial_number', 'make'):
        writer.writerow(fields)

    return response

def export_set_up(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fields.csv"'


    writer = csv.writer(response)
    writer.writerow(['Setup Name','Device Type', 'Device Hostname', 'Serial Number', 'Device IP', 'Device MAC', 'Device Make/Model'])

    for fields in Setup.objects.all():
        list = []
        list.append(fields.setup_name)
        list.append(fields.device_type)
        list.append(fields.device_type.hostname)
        list.append(fields.device_type.serial_number)
        list.append(fields.device_type.ip)
        list.append(fields.device_type.mac)
        list.append(fields.device_type.make)
        writer.writerow(list)

    return response

def search_setup(request):
    #inward_list = Form1.objects.all()
    #inward_filter = InwardFilter(request.GET, queryset=inward_list)
    setup_list = Setup.objects.all()
    setup_filter = SetupFilter(request.GET, queryset=setup_list)
    return render(request, 'search_setup.html', {'filter': setup_filter })

def search_device(request):
    #inward_list = Form1.objects.all()
    #inward_filter = InwardFilter(request.GET, queryset=inward_list)
     device_list = Device.objects.all()
     device_filter = DeviceFilter(request.GET, queryset=device_list)
     return render(request, 'search_device.html', {'filter': device_filter })