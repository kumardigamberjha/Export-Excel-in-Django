# Generated by Django 4.0.3 on 2022-03-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=50)),
                ('Job_Title', models.CharField(max_length=50)),
                ('Salaries_Reported', models.IntegerField()),
                ('Location', models.CharField(max_length=50)),
                ('Salary', models.CharField(max_length=20)),
            ],
        ),
    ]
