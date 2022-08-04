from curses.ascii import NUL
from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.

class ToDoList(models.Model):
    statuss=[
       ( 'new','New'),
        ('progress','Progress'),
        ('done','Done'),
        ('rejected','Rejected')
    ]
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    status = models.CharField(choices=statuss, max_length=10, default=statuss[0][0])
    start_time = models.DateTimeField()
    started_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    ended_time = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'ToDolist'
        verbose_name_plural ='ToDoLists'

