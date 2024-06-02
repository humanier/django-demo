from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
