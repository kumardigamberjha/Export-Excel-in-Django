from import_export import resources

from .models import SalaryModel

class SalaryResources(resources.ModelResource):
    class Meta:
        model = SalaryModel
        fields = ['Company_Name', 'Job_Title', 'Salaries_Reported', 'Location', 'Salary']