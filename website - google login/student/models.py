from django.db import models


class Classz(models.Model):
    division = models.CharField(max_length=1)

    def __str__(self):
        return self.division

class Student(models.Model):
    classz = models.ForeignKey(Classz, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    rollno = models.CharField(max_length=25)
    marks = models.IntegerField()

    def __str__(self):
        return self.name


