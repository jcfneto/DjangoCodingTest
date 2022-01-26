from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    salary = models.FloatField(blank=True, null=True)
    first_day = models.DateField(null=True, blank=True)

    class Meta:

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.name} - {self.department}'
