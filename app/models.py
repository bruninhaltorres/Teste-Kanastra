from django.db import models

class Person(models.Model):

    name = models.CharField(max_length=30, blank=False, null=False)
    governmentId = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    debtAmount = models.DecimalField(max_digits=38, decimal_places=2)
    debtDueDate = models.DateField()

    def __str__(self):
        """Cada usuario sera representado pelo nome"""
        return self.name
