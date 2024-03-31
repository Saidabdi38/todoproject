from django.db import models

# Create your models here.
status = [
        ("Completed", "Completed"), 
        ("Not Completed", "Not Completed"), 
]
    
class Shaqada(models.Model):
    shaqada = models.CharField(max_length=150)

    def __str__(self):
        return self.shaqada

class Task(models.Model):
    fullname = models.CharField(max_length=250, blank=False)
    tel = models.CharField(max_length=250, blank=False)
    zoone = models.CharField(max_length=100,blank=False)
    shaqada = models.ForeignKey(Shaqada, blank=False, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField(blank=False)
    completion = models.CharField(max_length=200, choices=status, default='Not Completed')
    memo = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.fullname   