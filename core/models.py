from django.db import models


class Department(models.Model):

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateField()

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class Employee(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    birth_date = models.DateField()
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    first_day = models.DateField()

    class Meta:

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.name} - {self.department}'
