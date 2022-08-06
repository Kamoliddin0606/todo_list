from curses.ascii import NUL
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model):
    statuss=[
       ( 'new','New'),
        ('progress','Progress'),
        ('done','Done'),
        ('rejected','Rejected')
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    progress = models.BooleanField(default=False)
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

