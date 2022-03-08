from django.db import models

class SalaryModel(models.Model):
    Company_Name = models.CharField(max_length=50)
    Job_Title = models.CharField(max_length=50)
    Salaries_Reported = models.IntegerField()
    Location = models.CharField(max_length=50)
    Salary = models.CharField(max_length=20)

    def __str__(self):
        return self.Company_Name