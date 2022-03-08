from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import SalaryModel
from .resource import SalaryResources
from tablib import Dataset
from django.contrib import messages

def index(request):
    if request.method == "POST":
        sal_res = SalaryResources()
        dataset = Dataset()
        new_sal = request.FILES.get('myFiles')
        print("salaary: ",new_sal)

        if not new_sal.name.endswith("xlsx"):
            messages.info(request, 'Wrong Format')
            return render(request, 'website/index.html')

        imported_data = dataset.load(new_sal.read(), format='xlsx')
        for data in imported_data:
            value = SalaryModel(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
            )
            value.save()
    return render(request, 'website/index.html')

def ExportFile(request):
    salary_resource = SalaryResources()
    dataset = salary_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="salary.xls"'
    return response
