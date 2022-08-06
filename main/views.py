from concurrent.futures import process
from math import fabs
from django.shortcuts import redirect, render
from .models import *
from .forms import ToDoForm
# Create your views here.

def index(request, id=None):
    print("____________",request.user.is_authenticated)
    if request.user.is_authenticated:

        form =ToDoForm()
        update =False
        list_new = ToDoList.objects.filter(done=False, rejected=False, progress=False, author=request.user)
        list_done = ToDoList.objects.filter(done=True, rejected=False, progress=False, author=request.user)
        list_reject = ToDoList.objects.filter(done=False, rejected=True, progress=False, author=request.user)
        list_progress = ToDoList.objects.filter(done=False, rejected=False, progress=True, author=request.user)

        if request.method == 'POST':
            
            try:

                id =int(request.POST.get('update'))
                form = ToDoForm(request.POST, instance=ToDoList.objects.get(id=id))
                if form.is_valid():
                    form.save()
                    return redirect('index')

                
            except:
                form = ToDoForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('index')
                

        if id:
            update=id
            form = ToDoForm(instance=ToDoList.objects.get(id=id))
        context = {
            'list_new':list_new,
            'list_done':list_done,
            'list_reject':list_reject,
            'list_progress':list_progress,
            'update':update,
            'form': form,

        }
        return render(request=request, template_name='main/index.html', context=context)
    else:
        return redirect('login')
def done(request, id):
    task = ToDoList.objects.filter(id=id).update(done=True, rejected=False, progress=False)
    return redirect('index')
def remove(request, id):
    task = ToDoList.objects.get(id=id).delete()
    return redirect('index')
def reject(request, id):
    task = ToDoList.objects.filter(id=id).update(done=False, rejected=True, progress=False)
    return redirect('index')
def start(request, id):
    task = ToDoList.objects.get(id=id)
    if task.done !=True and task.rejected != True and task.progress != True:

        task = ToDoList.objects.filter(id=id).update(progress = True)

    return redirect('index')