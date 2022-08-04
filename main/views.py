from django.shortcuts import redirect, render
from .models import *
from .forms import ToDoForm
# Create your views here.

def index(request):
    form =ToDoForm()

    todolist = ToDoList.objects.all()

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'todolist':todolist,
        'form': form,

    }
    return render(request=request, template_name='main/index.html', context=context)
def done(request, id):
    task = ToDoList.objects.filter(id=id).update(done=True, rejected=False)
    return redirect('index')
def remove(request, id):
    task = ToDoList.objects.get(id=id).delete()
    return redirect('index')
def reject(request, id):
    task = ToDoList.objects.filter(id=id).update(done=False, rejected=True)
    return redirect('index')