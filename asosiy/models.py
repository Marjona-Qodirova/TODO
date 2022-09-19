from django.contrib.auth.models import User
from django.db import models



class Student(models.Model):
    ism=models.CharField(max_length=50)
    yosh = models.IntegerField()
    kurs = models.IntegerField()
    student_number = models.CharField(max_length=30, blank=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.ism
class Rejalar(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE, null=True)
    sarlavha=models.CharField(max_length=100)
    batafsil=models.TextField()
    status=models.CharField(max_length=12, default="Yangi")
    sana = models.DateField()
    bajarilmagan = models.BooleanField(default=False)
    def __str__(self):
        return self.sarlavha


