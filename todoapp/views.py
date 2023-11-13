from django.shortcuts import render, redirect
from todoapp.models import Task
# Create your views here.

def home(request):
    task = Task.objects.filter(is_item_complate=False)
    task2 = Task.objects.filter(is_item_complate=True)
    if request.method =='POST':
        item = request.POST['item']
        Task.objects.create(item=item)
        return redirect('home')
    else:
        return render(request, 'todo.html', {'task': task, 'task2': task2})
def edit_todo(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.item = request.POST.get('item')
        task.save() 
        return redirect('home')
    return render(request, 'edit_todo.html', {'task':task})
def itemdelete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')

def markdone(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_item_complate = True
    task.save()
    return redirect('home')